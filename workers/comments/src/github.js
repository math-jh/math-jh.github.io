import {
  PublicError, base64ToUtf8, parseCommentYaml, serializeTombstone,
  threadPermalink, threadTitle, utf8ToBase64
} from "./lib.js";

function apiBase(env) {
  return `https://api.github.com/repos/${encodeURIComponent(env.GITHUB_OWNER)}/${encodeURIComponent(env.GITHUB_REPO)}`;
}

async function githubOrNull(env, path, options = {}) {
  try {
    return await github(env, path, options);
  } catch (error) {
    if (error.status === 404) return null;
    throw error;
  }
}

async function github(env, path, options = {}) {
  const response = await fetch(`${apiBase(env)}${path}`, {
    ...options,
    headers: {
      accept: "application/vnd.github+json",
      authorization: `Bearer ${env.GITHUB_TOKEN}`,
      "content-type": "application/json",
      "user-agent": "math-jh-comments-worker",
      "x-github-api-version": "2022-11-28",
      ...options.headers
    }
  });
  if (!response.ok) {
    const error = new Error(`GitHub API ${response.status}`);
    error.status = response.status;
    throw error;
  }
  if (response.status === 204) return null;
  return response.json();
}

function contentPath(path) {
  return path.split("/").map(encodeURIComponent).join("/");
}

export async function getBranchSha(env) {
  const ref = await github(env, `/git/ref/heads/${encodeURIComponent(env.GITHUB_BRANCH || "main")}`);
  return ref.object.sha;
}

export async function createCommentPullRequest(env, { comment, path, yaml, parent }) {
  const branch = `comment/${comment.id}`;
  const base = env.GITHUB_BRANCH || "main";
  let branchCreated = false;
  try {
    const sha = await getBranchSha(env);
    await github(env, "/git/refs", {
      method: "POST",
      body: JSON.stringify({ ref: `refs/heads/${branch}`, sha })
    });
    branchCreated = true;
    await github(env, `/contents/${contentPath(path)}`, {
      method: "PUT",
      body: JSON.stringify({
        message: `댓글 추가: ${comment.id}`,
        content: utf8ToBase64(yaml),
        branch
      })
    });
    const permalink = threadPermalink(comment.thread);
    const parentQuote = parent
      ? `\n\n부모 댓글: ${parent.id} — ${String(parent.message || "").slice(0, 240)}`
      : "";
    const pull = await github(env, "/pulls", {
      method: "POST",
      body: JSON.stringify({
        title: `댓글: ${comment.name} — ${threadTitle(comment.thread)}`,
        head: branch,
        base,
        body: [
          `스레드: https://math-jh.com${permalink}`,
          `댓글 ID: ${comment.id}${parentQuote}`,
          "",
          "자동 판정: Turnstile·honeypot·체류시간·필드·HTML·링크 상한 통과"
        ].join("\n")
      })
    });
    return { number: pull.number, url: pull.html_url, branch };
  } catch (error) {
    if (branchCreated) {
      await deleteBranch(env, branch).catch(() => {});
    }
    throw error;
  }
}

export async function deleteBranch(env, branch) {
  return github(env, `/git/refs/heads/${encodeURIComponent(branch)}`, { method: "DELETE" });
}

// 수정은 승인된 댓글의 파일을 main 에 바로 덮지 않는다 — 그러면 무해한 댓글로 승인을
// 받은 뒤 나중에 내용을 갈아치우는 경로가 열린다. 대신 comment-edit/<id> 브랜치의
// PR 로 올리고, 같은 댓글을 다시 고치면 그 브랜치·PR 을 재사용한다.
export async function createCommentEditPullRequest(env, { comment, path, yaml, previous }) {
  const branch = `comment-edit/${comment.id}`;
  const base = env.GITHUB_BRANCH || "main";
  let branchCreated = false;
  try {
    const sha = await getBranchSha(env);
    const created = await github(env, "/git/refs", {
      method: "POST",
      body: JSON.stringify({ ref: `refs/heads/${branch}`, sha })
    }).catch((error) => {
      // 422 = 브랜치가 이미 있다(같은 댓글의 두 번째 수정). 그대로 이어 쓴다.
      if (error.status === 422) return null;
      throw error;
    });
    branchCreated = Boolean(created);

    // 덮어쓸 blob 의 sha 는 **브랜치 기준**이어야 한다. main 의 sha 로 PUT 하면
    // 두 번째 수정이 409 로 튕긴다.
    const onBranch = await githubOrNull(
      env,
      `/contents/${contentPath(path)}?ref=${encodeURIComponent(branch)}`
    );
    await github(env, `/contents/${contentPath(path)}`, {
      method: "PUT",
      body: JSON.stringify({
        message: `댓글 수정: ${comment.id}`,
        content: utf8ToBase64(yaml),
        sha: onBranch?.sha || previous._sha,
        branch
      })
    });

    const existing = await findOpenPullRequest(env, branch);
    if (existing) return { number: existing.number, url: existing.html_url, branch, reused: true };

    const permalink = threadPermalink(comment.thread);
    const pull = await github(env, "/pulls", {
      method: "POST",
      body: JSON.stringify({
        title: `댓글 수정: ${comment.name} — ${threadTitle(comment.thread)}`,
        head: branch,
        base,
        body: [
          `스레드: https://math-jh.com${permalink}`,
          `댓글 ID: ${comment.id}`,
          "",
          "수정 전 본문:",
          "",
          "```",
          String(previous.message || "").slice(0, 2000),
          "```",
          "",
          "자동 판정: 삭제용 암호 일치 · HTML·링크 상한 통과"
        ].join("\n")
      })
    });
    return { number: pull.number, url: pull.html_url, branch, reused: false };
  } catch (error) {
    if (branchCreated) await deleteBranch(env, branch).catch(() => {});
    throw error;
  }
}

async function getDirectory(env, thread) {
  try {
    const value = await github(
      env,
      `/contents/${contentPath(`_data/comments/${thread}`)}?ref=${encodeURIComponent(env.GITHUB_BRANCH || "main")}`
    );
    return Array.isArray(value) ? value : [];
  } catch (error) {
    if (error.status === 404) return [];
    throw error;
  }
}

export async function getThreadComments(env, thread) {
  const entries = (await getDirectory(env, thread))
    .filter((entry) => entry.type === "file" && /^comment-.*\.ya?ml$/.test(entry.name));
  return Promise.all(entries.map(async (entry) => {
    const file = await github(
      env,
      `/contents/${contentPath(entry.path)}?ref=${encodeURIComponent(env.GITHUB_BRANCH || "main")}`
    );
    return {
      ...parseCommentYaml(base64ToUtf8(file.content)),
      _path: entry.path,
      _sha: file.sha
    };
  }));
}

export async function assertReferencesExist(env, comment) {
  const wanted = new Set([comment.replying_to, ...comment.mentions].filter(Boolean));
  if (!wanted.size) return { comments: [], parent: null };
  const comments = await getThreadComments(env, comment.thread);
  const found = new Set(comments.filter((item) => !item.deleted).map((item) => item.id));
  if ([...wanted].some((id) => !found.has(id))) throw new PublicError(400, "unknown_reference");
  const parent = comment.replying_to
    ? comments.find((item) => item.id === comment.replying_to)
    : null;
  if (parent?.replying_to) throw new PublicError(400, "invalid_reply_target");
  return {
    comments,
    parent
  };
}

export async function findOpenPullRequest(env, branch) {
  const head = `${env.GITHUB_OWNER}:${branch}`;
  const pulls = await github(env, `/pulls?state=open&head=${encodeURIComponent(head)}`);
  return pulls[0] || null;
}

export async function findOpenCommentPullRequest(env, id) {
  return findOpenPullRequest(env, `comment/${id}`);
}

// 삭제는 열려 있는 수정 PR 도 같이 닫아야 한다. 남겨두면 나중에 머지될 때
// 지운 댓글이 되살아난다.
export async function closePendingEdit(env, id) {
  const branch = `comment-edit/${id}`;
  const pull = await findOpenPullRequest(env, branch);
  if (pull) {
    await github(env, `/pulls/${pull.number}`, {
      method: "PATCH",
      body: JSON.stringify({ state: "closed" })
    });
  }
  await deleteBranch(env, branch).catch(() => {});
  return Boolean(pull);
}

export async function closePendingComment(env, id) {
  const pull = await findOpenCommentPullRequest(env, id);
  if (!pull) return false;
  await github(env, `/pulls/${pull.number}`, {
    method: "PATCH",
    body: JSON.stringify({ state: "closed" })
  });
  await deleteBranch(env, `comment/${id}`);
  return true;
}

export async function deleteApprovedComment(env, id, thread) {
  const comments = await getThreadComments(env, thread);
  const target = comments.find((comment) => comment.id === id);
  if (!target) return null;
  const hasDependents = comments.some((comment) =>
    comment.id !== id && (
      comment.replying_to === id || (Array.isArray(comment.mentions) && comment.mentions.includes(id))
    )
  );
  if (hasDependents) {
    await github(env, `/contents/${contentPath(target._path)}`, {
      method: "PUT",
      body: JSON.stringify({
        message: `댓글 tombstone 처리: ${id}`,
        content: utf8ToBase64(serializeTombstone(target)),
        sha: target._sha,
        branch: env.GITHUB_BRANCH || "main"
      })
    });
    return "tombstone";
  }
  await github(env, `/contents/${contentPath(target._path)}`, {
    method: "DELETE",
    body: JSON.stringify({
      message: `댓글 삭제: ${id}`,
      sha: target._sha,
      branch: env.GITHUB_BRANCH || "main"
    })
  });
  return "deleted";
}

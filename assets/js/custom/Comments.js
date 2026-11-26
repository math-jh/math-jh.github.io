// Anonymous static comments: submission, one-level replies, structured mentions,
// edit requests, and deletion-key UI. No jQuery and no third-party comment-provider
// assumptions.
window.commentsTurnstileLoaded = function () {
  document.dispatchEvent(new Event("comments:turnstile-ready"));
};

(function () {
  "use strict";

  // --- 안내(ⓘ): 호버·포커스는 CSS 가 연다. 여기서는 터치 기기용 클릭 토글만.
  function initInfoToggles() {
    document.querySelectorAll(".js-comment-info").forEach(function (info) {
      var infoToggle = info.querySelector(".js-comment-info-toggle");
      if (!infoToggle || infoToggle.dataset.bound) return;
      infoToggle.dataset.bound = "true";
      infoToggle.addEventListener("click", function () {
        var open = info.hasAttribute("data-open");
        if (open) info.removeAttribute("data-open");
        else info.setAttribute("data-open", "");
        infoToggle.setAttribute("aria-expanded", open ? "false" : "true");
      });
      document.addEventListener("click", function (event) {
        if (!info.contains(event.target)) {
          info.removeAttribute("data-open");
          infoToggle.setAttribute("aria-expanded", "false");
        }
      });
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
          info.removeAttribute("data-open");
          infoToggle.setAttribute("aria-expanded", "false");
        }
      });
    });
  }

  // 댓글 목록과 사이드바 '최근 댓글'은 글 HTML 밖의 조각(/comments/…)에 있다. robots.txt 가
  // 그 경로를 막아 검색엔진은 댓글을 보지 못하고, 브라우저에서는 여기서 불러와 끼운다
  // (_plugins/comment_fragments.rb). data-src 가 없는 목록은 HTML 에 이미 들어 있는 것이다.
  function loadFragment(el) {
    return fetch(el.dataset.src, { credentials: "same-origin" }).then(function (response) {
      if (!response.ok) throw new Error("fragment " + response.status);
      return response.text();
    }).then(function (html) {
      el.innerHTML = html;
      return el;
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initInfoToggles();

    // 사이드바는 댓글 영역이 없는 페이지(목록·홈)에도 있으므로 root 검사보다 앞에 둔다.
    document.querySelectorAll(".js-recent-comments[data-src]").forEach(function (list) {
      loadFragment(list).catch(function () {
        list.innerHTML = '<li><span class="nav__recents-empty">—</span></li>';
      });
    });

    var root = document.querySelector(".js-comment-system");
    if (!root) return;

    var endpoint = (root.dataset.endpoint || "").replace(/\/$/, "");
    // dev 빌드(preview)에만 있다 — 있으면 쓰기·수정·삭제를 Worker 대신 대시보드 서버의
    // 운영자 경로로 보낸다 (_includes/comments-providers/custom.html :: _comment_owner).
    var ownerEndpoint = (root.dataset.ownerEndpoint || "").replace(/\/$/, "");
    var thread = root.dataset.thread || "";
    var lang = root.dataset.lang === "en" ? "en" : "ko";
    var form = root.querySelector(".js-comment-form");
    var respond = root.querySelector(".js-comment-respond");
    var anchor = root.querySelector(".js-comment-form-anchor");
    var notice = root.querySelector(".js-comment-notice");
    var context = root.querySelector(".js-comment-context");
    var cancelReply = root.querySelector(".js-cancel-reply");
    var chips = root.querySelector(".js-mention-chips");
    var submit = root.querySelector("#comment-form-submit");
    var turnstileContainer = root.querySelector(".js-comment-turnstile");
    var turnstileWidgetId = null;
    var turnstileToken = "";
    var mentions = new Map();
    var interactionAt = 0;

    if (!form || !respond || !anchor || !submit) return;

    function copy(ko, en) { return lang === "ko" ? ko : en; }

    // Worker 의 실패 코드를 문구로 옮긴다. 여기서 코드를 나누지 않으면 삭제·수정
    // 실패가 전부 "댓글을 제출하지 못했습니다"로 나온다.
    function messageForCode(code, fallback) {
      switch (code) {
        case "delete_auth_failed":
        case "invalid_delete_request":
          return root.dataset.authError;
        case "delete_locked":
          return root.dataset.lockedError;
        case "comment_not_found":
          return root.dataset.notFoundError;
        case "edit_unchanged":
          return root.dataset.editUnchanged;
        case "edit_too_soon":
          return root.dataset.editTooSoon;
        default:
          return fallback;
      }
    }

    var ownerSaved = copy(
      "처리했습니다. 미리보기에는 잠시 뒤 반영되고, autopush 가 다음 실행에 공개합니다.",
      "Done. The preview picks it up shortly; autopush publishes it on its next run.");

    // 대시보드 서버는 실패를 {ok:false, error:"<사람이 읽는 문장>"} 으로 준다. 응답이 JSON 이
    // 아니면 /dash/ 가 없는 호스트(chat.math-jh.com, :4001 직결)에서 연 것이다.
    async function ownerPost(action, body) {
      var response;
      try {
        response = await fetch(ownerEndpoint + "/" + action, {
          method: "POST",
          headers: { "content-type": "application/json", "X-Dash-Action": "1" },
          body: JSON.stringify(body)
        });
      } catch (_error) {
        throw new Error(copy("대시보드 서버에 닿지 못했습니다.", "Could not reach the dashboard server."));
      }
      var result = await response.json().catch(function () { return null; });
      if (response.ok && result && result.ok) return result;
      throw new Error((result && result.error) || copy(
        "운영자 댓글은 preview.math-jh.com 에서만 쓸 수 있습니다.",
        "Owner comments work only on preview.math-jh.com."));
    }

    function markInteraction() {
      if (!interactionAt) interactionAt = Date.now();
    }
    ["focusin", "pointerdown", "input"].forEach(function (eventName) {
      form.addEventListener(eventName, markInteraction, { once: true });
    });

    function showNotice(message, state) {
      notice.textContent = message;
      notice.dataset.state = state || "info";
      notice.hidden = false;
    }

    function clearNotice() {
      notice.hidden = true;
      notice.textContent = "";
      delete notice.dataset.state;
    }

    function setStatus(element, message, state) {
      element.textContent = message;
      if (state) element.dataset.state = state;
      else delete element.dataset.state;
    }

    // --- 작성 시각: 서버 조판은 KST(site.timezone)이고, 여기서 방문자 시간대로
    // 다시 쓴다. Intl 이 없거나 datetime 이 깨져 있으면 KST 표기가 그대로 남는다.
    function localizeDates() {
      if (typeof Intl === "undefined" || !Intl.DateTimeFormat) return;
      var formatter;
      var full;
      try {
        formatter = new Intl.DateTimeFormat("en-CA", {
          year: "numeric", month: "2-digit", day: "2-digit",
          hour: "2-digit", minute: "2-digit", hourCycle: "h23"
        });
        full = new Intl.DateTimeFormat(lang === "ko" ? "ko-KR" : "en-US", {
          dateStyle: "long", timeStyle: "long"
        });
      } catch (_error) {
        return;
      }
      root.querySelectorAll(".js-comment-time").forEach(function (node) {
        var value = new Date(node.getAttribute("datetime"));
        if (isNaN(value.getTime())) return;
        var parts = {};
        formatter.formatToParts(value).forEach(function (part) { parts[part.type] = part.value; });
        if (!parts.year || !parts.hour) return;
        node.textContent = parts.year + "-" + parts.month + "-" + parts.day +
          " " + parts.hour + ":" + parts.minute;
        node.title = full.format(value);
      });
    }
    localizeDates();



    // --- Turnstile: interaction-only 라 사람으로 판정된 방문자에겐 위젯이 뜨지 않고,
    // 확인이 필요할 때만 이 자리에 나타난다.
    function renderTurnstile() {
      if (!turnstileContainer || turnstileWidgetId !== null || !window.turnstile) return;
      turnstileWidgetId = window.turnstile.render(turnstileContainer, {
        sitekey: turnstileContainer.dataset.sitekey,
        action: turnstileContainer.dataset.action,
        theme: "auto",
        appearance: "interaction-only",
        callback: function (token) { turnstileToken = token; },
        "expired-callback": function () { turnstileToken = ""; },
        "error-callback": function () { turnstileToken = ""; }
      });
    }

    function resetTurnstile() {
      turnstileToken = "";
      if (window.turnstile && turnstileWidgetId !== null) {
        window.turnstile.reset(turnstileWidgetId);
      }
    }

    document.addEventListener("comments:turnstile-ready", renderTurnstile, { once: true });
    renderTurnstile();

    // 확인은 페이지를 떠나지 않는다. Worker 의 확인 페이지는 메일 링크 전용이다.
    var confirmBox = root.querySelector(".js-comment-confirm");
    var confirmMessage = root.querySelector(".js-confirm-message");

    var confirmSubmit = root.querySelector(".js-confirm-submit");
    var confirmSubmitLabel = confirmSubmit ? confirmSubmit.textContent : "";

    function confirmAction(message, submitLabel) {
      if (!confirmBox || typeof confirmBox.showModal !== "function") {
        return Promise.resolve(window.confirm(message));
      }
      confirmSubmit.textContent = submitLabel || confirmSubmitLabel;
      confirmMessage.textContent = message;
      confirmBox.returnValue = "";
      confirmBox.showModal();
      return new Promise(function (resolve) {
        confirmBox.addEventListener("close", function () {
          resolve(confirmBox.returnValue === "confirm");
        }, { once: true });
      });
    }

    if (confirmBox) {
      // 배경(dialog 자신)을 누르면 취소로 닫는다.
      confirmBox.addEventListener("click", function (event) {
        if (event.target === confirmBox) confirmBox.close("cancel");
      });
    }

    function showSubmitted(deleteToken) {
      showNotice(root.dataset.success, "success");
      if (!deleteToken) return;
      notice.appendChild(document.createTextNode(" "));
      var button = document.createElement("button");
      button.type = "button";
      button.className = "comment-form__pending-delete";
      button.textContent = root.dataset.pendingDelete;
      button.addEventListener("click", function () { withdrawPending(deleteToken, button); });
      notice.appendChild(button);
    }

    async function withdrawPending(deleteToken, button) {
      if (!(await confirmAction(root.dataset.pendingDeleteConfirm, root.dataset.pendingDelete))) return;
      button.disabled = true;
      try {
        var response = await fetch(endpoint + "/v1/delete", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ token: deleteToken, confirm: true })
        });
        var result = await response.json().catch(function () { return {}; });
        if (!response.ok || !result.ok) throw new Error(result.code || "delete_failed");
        showNotice(root.dataset.pendingDeleteDone, "success");
      } catch (error) {
        showNotice(messageForCode(error.message, root.dataset.pendingDeleteError), "error");
        button.disabled = false;
      }
    }

    function setBusy(busy) {
      submit.disabled = busy;
      form.setAttribute("aria-busy", busy ? "true" : "false");
      submit.textContent = busy
        ? copy("제출 중…", "Submitting…")
        : copy("댓글 제출", "Submit comment");
    }

    function renderMentions() {
      chips.replaceChildren();
      mentions.forEach(function (name, id) {
        var chip = document.createElement("span");
        chip.className = "mention-chip";
        chip.textContent = "@" + name + " ";
        var remove = document.createElement("button");
        remove.type = "button";
        remove.className = "mention-chip__remove";
        remove.setAttribute("aria-label", copy(name + " 멘션 제거", "Remove mention of " + name));
        remove.textContent = "×";
        remove.addEventListener("click", function () {
          mentions.delete(id);
          renderMentions();
        });
        chip.appendChild(remove);
        chips.appendChild(chip);
      });
    }

    function resetReply() {
      form.elements.replying_to.value = "";
      context.hidden = true;
      context.textContent = "";
      cancelReply.hidden = true;
      anchor.insertAdjacentElement("afterend", respond);
    }

    // 한 댓글에서 수정·삭제 폼이 동시에 열리지 않게 한다.
    function closeInlineForms(except) {
      root.querySelectorAll(".js-comment-edit-form, .js-comment-delete-form").forEach(function (item) {
        if (item !== except) item.hidden = true;
      });
    }

    root.addEventListener("click", function (event) {
      var replyButton = event.target.closest(".js-comment-reply");
      if (replyButton) {
        var rootId = replyButton.dataset.rootId;
        var author = replyButton.dataset.author;
        var targetThread = root.querySelector('.comment-thread[data-root-id="' + CSS.escape(rootId) + '"]');
        if (!targetThread) return;
        form.elements.replying_to.value = rootId;
        context.textContent = copy(author + "님에게 답글", "Replying to " + author);
        context.hidden = false;
        cancelReply.hidden = false;
        targetThread.insertAdjacentElement("afterend", respond);
        form.elements.message.focus();
        return;
      }

      var mentionButton = event.target.closest(".js-comment-mention");
      if (mentionButton) {
        if (!mentions.has(mentionButton.dataset.commentId) && mentions.size >= 3) {
          showNotice(copy("멘션은 3개까지 추가할 수 있습니다.", "You can add up to three mentions."), "error");
          return;
        }
        mentions.set(mentionButton.dataset.commentId, mentionButton.dataset.author);
        renderMentions();
        form.elements.message.focus();
        return;
      }

      var editToggle = event.target.closest(".js-comment-edit-toggle");
      if (editToggle) {
        var editForm = editToggle.closest(".js-comment").querySelector(".js-comment-edit-form");
        var opening = editForm.hidden;
        closeInlineForms(opening ? editForm : null);
        editForm.hidden = !opening;
        if (opening) {
          // 원본 마크다운은 data-source 에만 있다 (렌더된 HTML 에서 되돌릴 수 없다).
          editForm.elements.message.value = editForm.dataset.source || "";
          setStatus(editForm.querySelector(".js-edit-notice"), "");
          editForm.elements.message.focus();
        }
        return;
      }

      var editCancel = event.target.closest(".js-comment-edit-cancel");
      if (editCancel) {
        editCancel.closest(".js-comment-edit-form").hidden = true;
        return;
      }

      var deleteToggle = event.target.closest(".js-comment-delete-toggle");
      if (deleteToggle) {
        var deleteForm = deleteToggle.closest(".js-comment").querySelector(".js-comment-delete-form");
        var showing = deleteForm.hidden;
        closeInlineForms(showing ? deleteForm : null);
        deleteForm.hidden = !showing;
        if (showing && deleteForm.elements.password) deleteForm.elements.password.focus();
      }
    });

    cancelReply.addEventListener("click", resetReply);

    form.addEventListener("submit", async function (event) {
      event.preventDefault();
      clearNotice();
      if (ownerEndpoint) {
        if (!form.reportValidity()) return;
        setBusy(true);
        try {
          await ownerPost("new", {
            thread: thread,
            message: form.elements.message.value,
            replying_to: form.elements.replying_to.value,
            mentions: Array.from(mentions.keys())
          });
          form.reset();
          mentions.clear();
          renderMentions();
          resetReply();
          showNotice(ownerSaved, "success");
        } catch (error) {
          showNotice(error.message, "error");
        } finally {
          setBusy(false);
        }
        return;
      }
      if (!endpoint || submit.dataset.missingTurnstile === "true") {
        showNotice(root.dataset.configError, "error");
        return;
      }
      var elapsed = interactionAt ? Date.now() - interactionAt : 0;
      if (elapsed < 3000) {
        showNotice(root.dataset.tooFast, "error");
        return;
      }
      if (!form.reportValidity()) return;
      var payload = {
        turnstile_token: turnstileToken,
        honeypot: form.elements.honeypot.value,
        elapsed_ms: elapsed,
        name: form.elements.name.value,
        password: form.elements.password.value,
        email: form.elements.email.value,
        message: form.elements.message.value,
        thread: thread,
        replying_to: form.elements.replying_to.value,
        mentions: Array.from(mentions.keys())
      };
      setBusy(true);
      try {
        var response = await fetch(endpoint + "/v1/comment", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(payload)
        });
        var result = await response.json().catch(function () { return {}; });
        if (!response.ok || !result.ok) throw new Error("submission_failed");
        form.reset();
        mentions.clear();
        renderMentions();
        resetReply();
        interactionAt = 0;
        resetTurnstile();
        showSubmitted(result.delete_token);
      } catch (_error) {
        showNotice(root.dataset.error, "error");
        resetTurnstile();
      } finally {
        setBusy(false);
      }
    });

    // 수정·삭제 폼은 댓글마다 있어 목록이 들어온 뒤에 묶는다 (클릭은 root 위임이라 따로 안 묶는다).
    function bindCommentForms(scope) {
    scope.querySelectorAll(".js-comment-edit-form").forEach(function (editForm) {
      editForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        var article = editForm.closest(".js-comment");
        var editNotice = editForm.querySelector(".js-edit-notice");
        if (!editForm.reportValidity()) return;
        var button = editForm.querySelector('button[type="submit"]');
        button.disabled = true;
        setStatus(editNotice, "");
        try {
          if (ownerEndpoint) {
            await ownerPost("edit", {
              id: article.dataset.commentId,
              thread: thread,
              message: editForm.elements.message.value
            });
            setStatus(editNotice, ownerSaved, "success");
            return;
          }
          var response = await fetch(endpoint + "/v1/edit", {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify({
              id: article.dataset.commentId,
              thread: thread,
              password: editForm.elements.password.value,
              message: editForm.elements.message.value
            })
          });
          var result = await response.json().catch(function () { return {}; });
          if (!response.ok || !result.ok) throw new Error(result.code || "edit_failed");
          editForm.elements.password.value = "";
          // 이 자리에서 본문을 바꾸지 않는다 — 수정은 PR 이 머지돼야 반영된다.
          setStatus(editNotice, root.dataset.editSuccess, "success");
        } catch (error) {
          setStatus(editNotice, ownerEndpoint ? error.message
            : messageForCode(error.message, root.dataset.editError), "error");
        } finally {
          button.disabled = false;
        }
      });
    });

    scope.querySelectorAll(".js-comment-delete-form").forEach(function (deleteForm) {
      deleteForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        var article = deleteForm.closest(".js-comment");
        var deleteNotice = deleteForm.querySelector(".js-delete-notice");
        if (!deleteForm.reportValidity()) return;
        if (!(await confirmAction(root.dataset.deleteConfirm))) return;
        var button = deleteForm.querySelector('button[type="submit"]');
        button.disabled = true;
        setStatus(deleteNotice, "");
        try {
          if (ownerEndpoint) {
            await ownerPost("delete", { id: article.dataset.commentId, thread: thread });
            setStatus(deleteNotice, ownerSaved, "success");
            return;
          }
          var response = await fetch(endpoint + "/v1/delete", {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify({
              id: article.dataset.commentId,
              thread: thread,
              password: deleteForm.elements.password.value,
              confirm: true
            })
          });
          var result = await response.json().catch(function () { return {}; });
          if (!response.ok || !result.ok) throw new Error(result.code || "delete_failed");
          deleteForm.elements.password.value = "";
          setStatus(deleteNotice, root.dataset.deleteSuccess, "success");
        } catch (error) {
          setStatus(deleteNotice, ownerEndpoint ? error.message
            : messageForCode(error.message, root.dataset.deleteError), "error");
        } finally {
          button.disabled = false;
        }
      });
    });
    }

    // 조각으로 들어온 목록은 페이지의 KaTeX auto-render(scripts.html, DOMContentLoaded)보다
    // 늦으므로 따로 렌더한다. 옵션은 scripts.html 과 같게 둔다.
    function renderMath(scope) {
      if (typeof window.renderMathInElement !== "function") return;
      window.renderMathInElement(scope, {
        delimiters: window.KATEX_DELIMITERS,
        macros: window.KATEX_MACROS,
        ignoredClasses: ["no-math"],
        strict: false,
        throwOnError: false
      });
    }

    // #comment-<id> 로 들어온 경우(사이드바 최근 댓글·알림 메일) 목록이 들어온 뒤에야 대상이 생긴다.
    function revealTarget() {
      if (location.hash.indexOf("#comment-") !== 0) return;
      var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target) target.scrollIntoView();
    }

    var list = root.querySelector(".js-comments");
    if (list && list.dataset.src) {
      list.setAttribute("aria-busy", "true");
      loadFragment(list).then(function () {
        list.removeAttribute("aria-busy");
        localizeDates();
        bindCommentForms(list);
        renderMath(list);
        revealTarget();
      }).catch(function () {
        list.removeAttribute("aria-busy");
        var failed = document.createElement("p");
        failed.className = "comment-list__empty";
        failed.textContent = copy("댓글을 불러오지 못했습니다.", "Could not load the comments.");
        list.replaceChildren(failed);
      });
    } else {
      bindCommentForms(root);
    }
  });
})();

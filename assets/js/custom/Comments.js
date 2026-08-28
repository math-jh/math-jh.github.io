// Anonymous static comments: submission, one-level replies, structured mentions,
// and deletion-key UI. No jQuery and no third-party comment-provider assumptions.
window.commentsTurnstileLoaded = function () {
  document.dispatchEvent(new Event("comments:turnstile-ready"));
};

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    var root = document.querySelector(".js-comment-system");
    if (!root) return;

    var endpoint = (root.dataset.endpoint || "").replace(/\/$/, "");
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

    function renderTurnstile() {
      if (!turnstileContainer || turnstileWidgetId !== null || !window.turnstile) return;
      turnstileWidgetId = window.turnstile.render(turnstileContainer, {
        sitekey: turnstileContainer.dataset.sitekey,
        action: turnstileContainer.dataset.action,
        theme: "auto",
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

    function showSubmitted(deleteToken) {
      showNotice(root.dataset.success, "success");
      if (!deleteToken) return;
      notice.appendChild(document.createTextNode(" "));
      var link = document.createElement("a");
      link.href = endpoint + "/v1/delete?t=" + encodeURIComponent(deleteToken);
      link.textContent = root.dataset.pendingDelete;
      link.rel = "nofollow";
      notice.appendChild(link);
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

      var deleteToggle = event.target.closest(".js-comment-delete-toggle");
      if (deleteToggle) {
        var deleteForm = deleteToggle.closest(".js-comment").querySelector(".js-comment-delete-form");
        deleteForm.hidden = !deleteForm.hidden;
        if (!deleteForm.hidden) deleteForm.elements.password.focus();
      }
    });

    cancelReply.addEventListener("click", resetReply);

    form.addEventListener("submit", async function (event) {
      event.preventDefault();
      clearNotice();
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

    root.querySelectorAll(".js-comment-delete-form").forEach(function (deleteForm) {
      deleteForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        var article = deleteForm.closest(".js-comment");
        var deleteNotice = deleteForm.querySelector(".js-delete-notice");
        if (!window.confirm(root.dataset.deleteConfirm)) return;
        var button = deleteForm.querySelector('button[type="submit"]');
        button.disabled = true;
        deleteNotice.textContent = "";
        try {
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
          if (!response.ok || !result.ok) throw new Error("delete_failed");
          deleteForm.elements.password.value = "";
          deleteNotice.dataset.state = "success";
          deleteNotice.textContent = root.dataset.deleteSuccess;
        } catch (_error) {
          deleteNotice.dataset.state = "error";
          deleteNotice.textContent = root.dataset.error;
        } finally {
          button.disabled = false;
        }
      });
    });
  });
})();

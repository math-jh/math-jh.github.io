(function () {
  "use strict";

  function initBackToTop() {
    var backToTop = document.querySelector(".sidebar__top");
    if (!backToTop) return;

    var framePending = false;

    function updateVisibility() {
      backToTop.classList.toggle("is-visible", window.scrollY >= window.innerHeight);
      framePending = false;
    }

    function requestUpdate() {
      if (framePending) return;
      framePending = true;
      window.requestAnimationFrame(updateVisibility);
    }

    window.addEventListener("scroll", requestUpdate, { passive: true });
    window.addEventListener("resize", requestUpdate, { passive: true });
    updateVisibility();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initBackToTop, { once: true });
  } else {
    initBackToTop();
  }
})();

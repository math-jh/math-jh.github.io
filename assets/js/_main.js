/* ==========================================================================
   jQuery plugin settings and other scripts
   ========================================================================== */

$(function() {
  // FitVids init
  $("#main").fitVids();

  // Sticky sidebar
  var stickySideBar = function() {
    var show =
      $(".author__urls-wrapper").find("button").length === 0
        ? $(window).width() > 1024 // width should match $large Sass variable
        : !$(".author__urls-wrapper").find("button").is(":visible");
    if (show) {
      // fix
      $(".sidebar").addClass("sticky");
    } else {
      // unfix
      $(".sidebar").removeClass("sticky");
    }
  };

  stickySideBar();

  $(window).resize(function() {
    stickySideBar();
  });

  // Follow menu drop down
  $(".author__urls-wrapper").find("button").on("click", function() {
    $(".author__urls").toggleClass("is--visible");
    $(".author__urls-wrapper").find("button").toggleClass("open");
  });

  // Close search screen with Esc key
  $(document).keyup(function(e) {
    if (e.keyCode === 27) {
      if ($(".initial-content").hasClass("is--hidden")) {
        $(".search-content").toggleClass("is--visible");
        $(".initial-content").toggleClass("is--hidden");
      }
    }
  });

  // Search toggle
  $(".search__toggle").on("click", function() {
    $(".search-content").toggleClass("is--visible");
    $(".initial-content").toggleClass("is--hidden");
    // set focus on input
    setTimeout(function() {
      $(".search-content").find("input").focus();
    }, 400);
  });

  // Smooth scrolling
  var scroll = new SmoothScroll('a[href*="#"]', {
    offset: 20,
    speed: 400,
    speedAsDuration: true,
    durationMax: 500
  });

  // Gumshoe scroll spy init
  if($("nav.toc").length > 0) {
    var spy = new Gumshoe("nav.toc a", {
      // Active classes
      navClass: "active", // applied to the nav list item
      contentClass: "active", // applied to the content

      // Nested navigation
      nested: false, // if true, add classes to parents of active link
      nestedClass: "active", // applied to the parent items

      // Offset & reflow
      offset: 20, // how far from the top of the page to activate a content area
      reflow: true, // if true, listen for reflows

      // Event support
      events: true // if true, emit custom events
    });

    // Move the short gold glow continuously along the neutral TOC rail. Each
    // marker represents the centre of its section (heading to next heading),
    // and the rail endpoints represent the article start/end. Gumshoe's
    // active item remains based on the section start.
    var tocMenu = document.querySelector("nav.toc .toc__menu");
    var tocProgressItems = tocMenu
      ? $(tocMenu).children("li").children("a").get().map(function(link) {
          var hash = link.hash;
          var id;
          var heading;

          if (!hash) return null;
          try {
            id = decodeURIComponent(hash.slice(1));
          } catch (error) {
            id = hash.slice(1);
          }

          heading = document.getElementById(id);
          return heading ? { link: link, heading: heading } : null;
        }).filter(function(item) {
          return item !== null;
        })
      : [];

    if (tocProgressItems.length > 0) {
      var tocSectionCenters = [];
      var tocMarkerCenters = [];
      var tocProgressAnchors = [];
      var tocRailAnchors = [];
      var tocProgressFrame = null;
      var tocMeasureFrame = null;
      var tocGlowHalfHeight = 1;
      var tocContent = document.querySelector(".page__content");

      var updateTocProgress = function() {
        var probe = window.pageYOffset + 20; // match Gumshoe's activation offset
        var current = 0;
        var next;
        var span;
        var progress = 0;
        var markerY;

        tocProgressFrame = null;

        while (
          current + 1 < tocProgressAnchors.length &&
          probe >= tocProgressAnchors[current + 1]
        ) {
          current += 1;
        }

        next = Math.min(current + 1, tocProgressAnchors.length - 1);
        span = tocProgressAnchors[next] - tocProgressAnchors[current];

        if (next !== current && span > 0) {
          progress = Math.max(
            0,
            Math.min(1, (probe - tocProgressAnchors[current]) / span)
          );
        }

        markerY = tocRailAnchors[current] +
          (tocRailAnchors[next] - tocRailAnchors[current]) * progress;

        tocMenu.style.setProperty("--toc-progress-y", markerY.toFixed(2) + "px");
        tocProgressItems.forEach(function(item, index) {
          var distance = Math.abs(tocMarkerCenters[index] - markerY) /
            tocGlowHalfHeight;
          var intensity;

          // Match the alpha stops of the rail's CSS gradient: full gold at
          // the centre, 65% at 30% of its half-height, then fade to neutral.
          if (distance >= 1) {
            intensity = 0;
          } else if (distance <= 0.3) {
            intensity = 1 - distance * (0.35 / 0.3);
          } else {
            intensity = 0.65 * (1 - (distance - 0.3) / 0.7);
          }

          item.link.style.setProperty(
            "--toc-marker-intensity",
            Math.max(0, Math.min(1, intensity)).toFixed(3)
          );
        });
        tocMenu.classList.add("is-progress-ready");
      };

      var requestTocProgress = function() {
        if (tocProgressFrame !== null) return;
        tocProgressFrame = window.requestAnimationFrame(updateTocProgress);
      };

      var measureTocProgress = function() {
        var menuRect = tocMenu.getBoundingClientRect();
        var glowStyle = window.getComputedStyle(tocMenu, "::after");
        var headingTops;
        var contentTop;
        var contentBottom;

        tocMeasureFrame = null;
        tocGlowHalfHeight = Math.max(1, parseFloat(glowStyle.height) / 2);
        headingTops = tocProgressItems.map(function(item) {
          return item.heading.getBoundingClientRect().top + window.pageYOffset;
        });
        contentTop = tocContent
          ? tocContent.getBoundingClientRect().top + window.pageYOffset
          : headingTops[0];
        contentBottom = tocContent
          ? tocContent.getBoundingClientRect().bottom + window.pageYOffset
          : document.documentElement.scrollHeight;
        tocSectionCenters = headingTops.map(function(top, index) {
          var end = index + 1 < headingTops.length
            ? headingTops[index + 1]
            : Math.max(top, contentBottom);
          return top + (end - top) / 2;
        });
        tocMarkerCenters = tocProgressItems.map(function(item) {
          var linkRect = item.link.getBoundingClientRect();
          return linkRect.top - menuRect.top + linkRect.height / 2;
        });
        tocProgressAnchors = [contentTop]
          .concat(tocSectionCenters, [contentBottom]);
        tocRailAnchors = [0]
          .concat(tocMarkerCenters, [tocMenu.offsetHeight]);

        requestTocProgress();
      };

      var requestTocMeasure = function() {
        if (tocMeasureFrame !== null) return;
        tocMeasureFrame = window.requestAnimationFrame(measureTocProgress);
      };

      window.addEventListener("scroll", requestTocProgress, { passive: true });
      window.addEventListener("resize", requestTocMeasure, { passive: true });
      window.addEventListener("load", requestTocMeasure);

      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(requestTocMeasure);
      }

      if ("ResizeObserver" in window) {
        if (tocContent) {
          var tocResizeObserver = new ResizeObserver(requestTocMeasure);
          tocResizeObserver.observe(tocContent);
        }
      }

      measureTocProgress();
    }
  }

  // add lightbox class to all image links
  $(
    "a[href$='.jpg'],a[href$='.jpeg'],a[href$='.JPG'],a[href$='.png'],a[href$='.gif'],a[href$='.webp']"
  ).has("> img").addClass("image-popup");

  // Magnific-Popup options
  $(".image-popup").magnificPopup({
    // disableOn: function() {
    //   if( $(window).width() < 500 ) {
    //     return false;
    //   }
    //   return true;
    // },
    type: "image",
    tLoading: "Loading image #%curr%...",
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      tError: '<a href="%url%">Image #%curr%</a> could not be loaded.'
    },
    removalDelay: 500, // Delay in milliseconds before popup is removed
    // Class that is added to body when popup is open.
    // make it unique to apply your CSS animations just to this exact popup
    mainClass: "mfp-zoom-in",
    callbacks: {
      beforeOpen: function() {
        // just a hack that adds mfp-anim class to markup
        this.st.image.markup = this.st.image.markup.replace(
          "mfp-figure",
          "mfp-figure mfp-with-anim"
        );
      }
    },
    closeOnContentClick: true,
    midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
  });

  // Add anchors for headings
  $('.page__content').find('h1, h2, h3, h4, h5, h6').each(function() {
    var id = $(this).attr('id');
    if (id) {
      var anchor = document.createElement("a");
      anchor.className = 'header-link';
      anchor.href = '#' + id;
      anchor.innerHTML = '<span class=\"sr-only\">Permalink</span><i class=\"material-icons\" style=\"vertical-align:-.2em\">link</i>';
      anchor.title = "Permalink";
      $(this).append(anchor);
    }
  });
});

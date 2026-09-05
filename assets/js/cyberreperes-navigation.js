/*
 * CyberRepères — Navigation de lecture
 *
 * Génère automatiquement :
 * - un sommaire latéral à partir des h2/h3 ;
 * - la section actuellement lue ;
 * - une progression de lecture ;
 * - un bouton de retour en haut.
 *
 * Le Markdown reste inchangé : les titres h2/h3 suffisent.
 */
(function () {
  "use strict";

  function initReadingNavigation() {
    const main = document.querySelector("main");
    const content = document.querySelector(".cr-reading-content");
    const aside = document.querySelector(".cr-reading-nav");
    const toc = document.querySelector(".cr-reading-toc");
    const progressBar = document.querySelector(".cr-reading-progress-bar");

    if (!main || !content || !aside || !toc || !progressBar) return;

    const headings = Array.from(content.querySelectorAll("h2, h3"))
      .filter(function (heading) {
        return !heading.closest(".comments");
      });

    /*
     * Seuil volontairement simple :
     * une page doit avoir une vraie structure pour afficher
     * la navigation latérale.
     */
    const h2Count = headings.filter(function (h) {
      return h.tagName === "H2";
    }).length;

    if (headings.length < 4 || h2Count < 2) {
      main.classList.add("cr-reading-nav-disabled");
      return;
    }

    // IDs stables et lisibles, sans dépendre du moteur Markdown.
    const usedIds = new Set();

    function slugify(text) {
      return text
        .toLocaleLowerCase("fr")
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/['’]/g, "")
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "");
    }

    headings.forEach(function (heading, index) {
      let id = heading.id || slugify(heading.textContent) || "section";
      let base = id;
      let suffix = 2;

      while (usedIds.has(id)) {
        id = base + "-" + suffix++;
      }

      heading.id = id;
      usedIds.add(id);

      const item = document.createElement("a");
      item.className = "cr-reading-toc-item cr-reading-toc-" +
        heading.tagName.toLowerCase();
      item.href = "#" + id;
      item.dataset.target = id;

      const number = document.createElement("span");
      number.className = "cr-reading-toc-number";
      number.textContent = String(index + 1).padStart(2, "0");

      const label = document.createElement("span");
      label.className = "cr-reading-toc-title";
      label.textContent = heading.textContent.trim();

      item.appendChild(number);
      item.appendChild(label);
      toc.appendChild(item);
    });

    const links = Array.from(toc.querySelectorAll("a"));

    // Indication de la section active.
    const observer = new IntersectionObserver(
      function (entries) {
        const visible = entries
          .filter(function (entry) { return entry.isIntersecting; })
          .sort(function (a, b) {
            return a.boundingClientRect.top - b.boundingClientRect.top;
          });

        if (!visible.length) return;

        const activeId = visible[0].target.id;
        links.forEach(function (link) {
          link.classList.toggle(
            "is-active",
            link.dataset.target === activeId
          );
        });
      },
      {
        root: null,
        rootMargin: "-16% 0px -68% 0px",
        threshold: 0
      }
    );

    headings.forEach(function (heading) {
      observer.observe(heading);
    });

    // Progression globale de la lecture.
    function updateProgress() {
      const rect = content.getBoundingClientRect();
      const viewportHeight = window.innerHeight;
      const start = window.scrollY + rect.top;
      const end = start + content.offsetHeight - viewportHeight;
      const value = end <= start
        ? 100
        : Math.min(100, Math.max(0, ((window.scrollY - start) / (end - start)) * 100));

      progressBar.style.width = value + "%";
    }

    // Bouton retour en haut.
    const backTop = document.createElement("button");
    backTop.type = "button";
    backTop.className = "cr-back-to-top";
    backTop.setAttribute("aria-label", "Revenir en haut de la page");
    backTop.innerHTML = "<span aria-hidden=\"true\">↑</span><span>Haut</span>";
    document.body.appendChild(backTop);

    function updateBackTop() {
      backTop.classList.toggle("is-visible", window.scrollY > 650);
    }

    backTop.addEventListener("click", function () {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });

    let ticking = false;
    function onScroll() {
      if (ticking) return;
      window.requestAnimationFrame(function () {
        updateProgress();
        updateBackTop();
        ticking = false;
      });
      ticking = true;
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", updateProgress);

    updateProgress();
    updateBackTop();

    main.classList.add("cr-reading-nav-enabled");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initReadingNavigation);
  } else {
    initReadingNavigation();
  }
})();

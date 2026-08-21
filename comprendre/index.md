---
layout: default
title: "Comprendre la cybersécurité industrielle"
nav_title: "Comprendre"
description: "Notions, acteurs et concepts pour comprendre la cybersécurité et les projets industriels."
nav: true
nav_order: 10
---
{% include comprendre-header.html %}

<div class="comprendre-view-switcher"> <button class="comprendre-view-button active" type="button" data-view="parcours"> Parcours </button> <button class="comprendre-view-button" type="button" data-view="recentes"> Dernières publications </button> </div>

{% assign pages_comprendre = site.pages
| where_exp: "page", "page.path contains 'comprendre/'"
%}

{% assign pages_editorial = pages_comprendre
| sort: "order"
%}

{% assign pages_recentes = pages_comprendre
| sort: "date"
| reverse
%}

{% assign pages_comprendre = site.pages
  | where_exp: "page", "page.path contains 'comprendre/'"
  | where_exp: "page", "page.path != 'comprendre/index.md'"
  | where_exp: "page", "page.order"
%}

{% assign pages_editorial = pages_comprendre
  | sort: "order"
%}

{% assign pages_recentes = pages_comprendre
  | sort: "date"
  | reverse
%}


<div class="comprendre-grid" data-view-container="parcours">

  {% assign current_chapter = "" %}

  {% for page in pages_editorial %}

    {% if page.chapter != current_chapter %}

      {% if current_chapter != "" %}
        </div>
      {% endif %}

      <div class="comprendre-chapter">
        <h3 class="comprendre-chapter-title">{{ page.chapter }}</h3>
      </div>

      <div class="comprendre-chapter-grid">

      {% assign current_chapter = page.chapter %}

    {% endif %}

    <a class="comprendre-card" href="{{ page.url | relative_url }}">
      <span class="comprendre-card-title">{{ page.title }} →</span>

      {% if page.description %}
      <span class="comprendre-card-description">
        {{ page.description }}
      </span>
      {% endif %}
    </a>

  {% endfor %}

  {% if current_chapter != "" %}
    </div>
  {% endif %}

</div>

<div class="comprendre-grid" data-view-container="recentes" style="display: none;">

{% for page in pages_recentes %}
{% unless page.path == "comprendre/index.md" %}

<a class="comprendre-card" href="{{ page.url | relative_url }}">
  <span class="comprendre-card-title">{{ page.title }} →</span>
  {% if page.description %}
  <span class="comprendre-card-description">{{ page.description }}</span>
  {% endif %}
  {% if page.date %}
  <span class="comprendre-card-date">
    {{ page.date | date: "%d/%m/%Y" }}
  </span>
  {% endif %}
</a>

{% endunless %}

{% endfor %}

</div>

À venir

<div class="comprendre-coming">

Cette rubrique sera progressivement enrichie avec notamment :

IT et OT
systèmes industriels
risque, menace et vulnérabilité
actifs et périmètres
défense en profondeur

</div>

<script> document.addEventListener("DOMContentLoaded", function () { const buttons = document.querySelectorAll(".comprendre-view-button"); const views = document.querySelectorAll("[data-view-container]"); buttons.forEach(function (button) { button.addEventListener("click", function () { const selectedView = button.dataset.view; buttons.forEach(function (item) { item.classList.remove("active"); }); button.classList.add("active"); views.forEach(function (view) { view.style.display = view.dataset.viewContainer === selectedView ? "" : "none"; }); }); }); }); </script>

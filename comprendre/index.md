---
layout: default
title: "Comprendre"
description: "Notions, acteurs et concepts pour comprendre la cybersécurité et les projets industriels."
nav: true
nav_order: 10
---

<div class="catalogue-intro catalogue-intro-comprendre">

  <div class="catalogue-intro-label">
    COMPRENDRE
  </div>

  <div class="catalogue-intro-content">
    <p>
La cybersécurité fait appel à de nombreuses notions, à des métiers et à des concepts qui peuvent parfois sembler abstraits. Cette rubrique présente les notions nécessaires pour comprendre les démarches de cybersécurité, particulièrement dans les environnements industriels.
    </p>

    <p>
L'objectif n'est pas de constituer un cours complet de cybersécurité, mais de donner les <strong>repères nécessaires pour comprendre les référentiels, les méthodes et les pratiques</strong> présentés sur CyberRepères.
    </p>
  </div>

</div>

## Notions et acteurs

<div class="comprendre-grid">

{% assign pages_comprendre = site.pages
  | where_exp: "page", "page.path contains 'comprendre/'"
  | sort: "title"
%}

{% for page in pages_comprendre %}
  {% unless page.path == "comprendre/index.md" %}

  <a class="comprendre-card" href="{{ page.url | relative_url }}">
    <span class="comprendre-card-title">{{ page.title }} →</span>
    {% if page.description %}
    <span class="comprendre-card-description">{{ page.description }}</span>
    {% endif %}
  </a>

  {% endunless %}
{% endfor %}

</div>

## À venir

<div class="comprendre-coming">

Cette rubrique sera progressivement enrichie avec notamment :

- IT et OT
- systèmes industriels
- risque, menace et vulnérabilité
- actifs et périmètres
- défense en profondeur

</div>

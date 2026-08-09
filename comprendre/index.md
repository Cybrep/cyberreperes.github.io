---
layout: default
title: "Comprendre"
description: "Notions, acteurs et concepts pour comprendre la cybersécurité et les projets industriels."
nav: true
nav_order: 10
---

# Comprendre
La cybersécurité fait appel à de nombreuses notions, à des métiers et à des concepts qui peuvent parfois sembler abstraits.
Cette rubrique présente les notions nécessaires pour comprendre les démarches de cybersécurité, particulièrement dans les environnements industriels.
L'objectif n'est pas de constituer un cours complet de cybersécurité, mais de donner les **repères nécessaires pour comprendre les référentiels, les méthodes et les pratiques** présentés sur CyberRepères.

---

## Notions et acteurs

{% assign pages_comprendre = site.pages
  | where_exp: "page", "page.path contains 'comprendre/'"
  | sort: "title" %}

{% for page in pages_comprendre %}
  {% unless page.path == "comprendre/index.md" %}
### [{{ page.title }} →]({{ page.url | relative_url }})

{{ page.description }}

  {% endunless %}
{% endfor %}

## À venir

Cette rubrique sera progressivement enrichie avec notamment :

- IT et OT
- systèmes industriels
- risque, menace et vulnérabilité
- actifs et périmètres
- défense en profondeur

---

**CyberRepères**
*Des références pour comprendre, des repères pour agir.*

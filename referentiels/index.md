layout: default
title: "Référentiels"
description: "Normes, standards, réglementations, guides et autres documents de référence pour la cybersécurité industrielle."
nav: true
nav_order: 20
---

# Référentiels

La cybersécurité industrielle s'appuie sur une littérature importante : normes, standards, réglementations, guides de bonnes pratiques, méthodes et publications d'organismes reconnus.
Cette rubrique a pour objectif de présenter ces documents, d'expliquer leur rôle et de les mettre en relation avec les pratiques et les livrables d'une démarche de cybersécurité.
---

## Normes et standards
Les normes et standards définissent des exigences, des principes ou des cadres de référence reconnus.

{% assign normes = site.pages
  | where: "type", "norme"
  | sort: "title" %}

{% if normes.size > 0 %}
{% for page in normes %}
### [{{ page.title }} →]({{ page.url | relative_url }})

{{ page.description }}

{% endfor %}
{% else %}
*Aucun document référencé dans cette catégorie pour le moment.*
{% endif %}
---

## Réglementation

Les textes réglementaires et législatifs susceptibles d'avoir un impact sur les organisations et les systèmes industriels.

{% assign reglementations = site.pages
  | where: "type", "reglementation"
  | sort: "title" %}

{% if reglementations.size > 0 %}
{% for page in reglementations %}
### [{{ page.title }} →]({{ page.url | relative_url }})

{{ page.description }}

{% endfor %}
{% else %}
*Aucun document référencé dans cette catégorie pour le moment.*
{% endif %}

---

## Guides et bonnes pratiques

Les guides, recommandations et publications destinés à accompagner la mise en œuvre concrète de la cybersécurité.

{% assign guides = site.pages
  | where: "type", "guide"
  | sort: "title" %}

{% if guides.size > 0 %}
{% for page in guides %}
### [{{ page.title }} →]({{ page.url | relative_url }})

{{ page.description }}

{% endfor %}
{% else %}
*Aucun document référencé dans cette catégorie pour le moment.*
{% endif %}

---

## Méthodes et référentiels méthodologiques

Les méthodes et cadres méthodologiques permettant d'analyser, d'évaluer ou de traiter les risques et les enjeux de cybersécurité.

{% assign methodes = site.pages
  | where: "type", "methode"
  | sort: "title" %}

{% if methodes.size > 0 %}
{% for page in methodes %}
### [{{ page.title }} →]({{ page.url | relative_url }})

{{ page.description }}

{% endfor %}
{% else %}
*Aucun document référencé dans cette catégorie pour le moment.*
{% endif %}

---

## Autres publications de référence

Cette catégorie regroupe les publications qui ne correspondent pas directement aux catégories précédentes : panoramas, études, retours d'expérience ou autres documents utiles.
{% assign autres = site.pages
  | where: "type", "publication"
  | sort: "title" %}

{% if autres.size > 0 %}
{% for page in autres %}
### [{{ page.title }} →]({{ page.url | relative_url }})

{{ page.description }}

{% endfor %}
{% else %}
*Aucun document référencé dans cette catégorie pour le moment.*
{% endif %}

---

## Comment utiliser cette rubrique ?

CyberRepères ne se substitue pas aux organismes qui publient ces documents.

Chaque fiche cherche à présenter :

- le rôle et l'objectif du document
- son domaine d'application
- son positionnement par rapport aux autres références
- les pratiques ou livrables auxquels il peut contribuer
- les relations avec d'autres documents
- sa source officielle et, lorsque cela est pertinent, ses différentes versions

Les documents officiels restent les références pour leur contenu, leurs exigences et leur interprétation.

---

**CyberRepères**

*Des références pour comprendre, des repères pour agir.*

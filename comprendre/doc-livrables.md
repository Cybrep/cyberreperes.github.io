---
layout: default
title: "Catalogue des livrables de cybersécurité industrielle"
description: "Identifier les documents, analyses et éléments de preuve utiles à la maîtrise de la cybersécurité des systèmes industriels."
category: "comprendre"
date: 2026-11-01
tags:
  - livrables
  - documentation
  - référentiels
  - IEC 62443
  - cybersécurité industrielle
revision: 2026-11-01
chapter: "Documentation"
order: 40
comments: true
---

# Catalogue des livrables de cybersécurité industrielle

La cybersécurité industrielle se traduit par des activités, des décisions et des mesures techniques. Pour être pilotées, vérifiées et maintenues dans le temps, celles-ci doivent également être **formalisées et tracées**.

Ce catalogue recense des documents, analyses, dossiers et éléments de preuve susceptibles d'être produits dans le cadre d'un projet industriel ou de l'exploitation d'un système OT.

Il a pour objectif d'aider les équipes projet, les exploitants, les métiers et les acteurs de la cybersécurité à répondre à plusieurs questions :

- Quels livrables prévoir pour maîtriser la cybersécurité d'un système industriel ?
- À quoi servent-ils et quelles activités permettent-ils de formaliser ?
- Quels référentiels ou textes peuvent justifier leur production ?
- Comment distinguer une exigence explicite d'un livrable utile pour démontrer un résultat attendu ?

Le catalogue est un **outil de repérage et de travail**. Il ne constitue ni une liste universelle de documents obligatoires, ni un modèle documentaire à appliquer systématiquement à chaque projet.

---

## Consulter le catalogue détaillé

Le fichier Excel constitue le support détaillé et évolutif du catalogue. Il présente, pour chaque livrable, son domaine, le niveau de besoin, les sources primaires identifiées, les éléments justifiant son intérêt, les dépendances possibles et les correspondances indicatives avec l'IEC 62443-2-1:2024.

[ Télécharger le catalogue des livrables – format Excel ]({{ '/comprendre/sources/CyberReperes_catalogue_livrables_v2.4.xlsx' | relative_url }})

---

## Comprendre les niveaux de besoin

Les livrables sont classés selon trois niveaux. Cette classification vise à éviter de présenter comme une obligation documentaire ce qui relève parfois d'un moyen d'ingénierie ou d'une bonne pratique.

### 1 — Exigence

Le texte réglementaire ou le référentiel applicable demande explicitement le document, l'information ou l'activité correspondante.

**Attention :** l'exigence dépend toujours du champ d'application du texte, du type d'entité, du système concerné et du contexte réglementaire ou contractuel.

### 2 — Induit

Le référentiel impose un objectif ou un résultat. Le livrable identifié constitue un moyen structuré et pertinent pour le démontrer, sans que le document soit nécessairement nommé ou imposé sous cette forme.

### 3 — Bonne pratique

Le livrable facilite le cadrage, la conception, la contractualisation, la vérification, la traçabilité ou le transfert vers l'exploitation. Aucune exigence explicite imposant ce document sous cette appellation n'a été identifiée dans les sources examinées.

### Une classification à contextualiser

Un même livrable peut changer de niveau selon le périmètre étudié. Une cartographie peut, par exemple, relever d'une exigence réglementaire pour un SIIV, tandis qu'elle répondra à un autre cadre d'exigences dans un environnement différent.

Le niveau indiqué dans le catalogue doit donc être lu avec les références et les réserves associées à chaque ligne. **L'absence d'une exigence explicite ne signifie pas qu'un livrable est inutile.**

---

## Panorama des livrables recensés

La liste ci-dessous donne une vue d'ensemble des livrables recensés dans la version 2.4 du catalogue. Les intitulés sont regroupés par grands domaines pour faciliter la lecture ; certains documents peuvent naturellement relever de plusieurs domaines.

### Gouvernance, conformité et gestion des risques

- Politique de sécurité des systèmes d'information (PSSI)
- Analyse de conformité du SI
- Analyse de risques
- Plan d'action de traitement des risques
- Dossier d'homologation
- Programme / stratégie d'exercices cyber
- Dossier des exigences cyber applicables
- Matrice de traçabilité des exigences
- Dossier de mesures compensatoires

### Architecture, cartographie et conception

- Cartographie des systèmes d'information
- Cartographie SIIV
- Cartographie et inventaires
- Dossier d'architecture technique (DAT)
- Réseau / architecture d'administration dédiée
- Dossier d'administration sécurisée
- Dossier d'interconnexion
- Architecture zones & conduits
- Dossier de conception logicielle sécurisée
- Dossier d'interfaces applicatives
- Dossier de configuration PLC

### Continuité, résilience et exploitation

- Plan de continuité d'activité (PCA) / Plan de reprise d'activité (PRA)
- DMIA / PRD documentés
- Analyse d'impact sur l'activité (BIA)
- Procédures de sauvegarde et restauration
- Dossier de résilience / analyse des points uniques de défaillance (SPOF)
- Dossier de transfert vers l'exploitation
- Dossier TQC / As-Built

### Configuration, maintien en condition et détection

- Revue de configuration
- Dossier / référentiel de configuration sécurisée
- Dossier de journalisation / supervision
- Dossier de gestion des vulnérabilités
- Dossier de gestion des changements / Management of Change (MoC)
- Gestion des programmes PLC
- Plan de vérification et validation cyber

### Assurance sécurité et audit

- Programme d'audit de sécurité
- Audit de sécurité
- Audit d'architecture
- Audit de configuration
- Rapport d'audit de sécurité
- Plan d'action issu des audits

### Prestataires et chaîne d'approvisionnement

- Plan d'assurance sécurité (PAS)
- Évaluation cyber fournisseur
- Matrice de conformité fournisseur
- Dossier de télémaintenance fournisseur
- Politique de sécurité de la chaîne d'approvisionnement
- Critères de sélection et de contractualisation des fournisseurs
- Plan de gestion des risques de la chaîne d'approvisionnement (C-SCRM)
- Dossier de surveillance et de réévaluation des fournisseurs
- SBOM / inventaire des composants logiciels

---

## Lire les correspondances avec l'IEC 62443

Le catalogue propose également des rapprochements entre les livrables et des exigences de l'**IEC 62443-2-1:2024**, notamment dans les domaines de l'organisation, de la gestion de configuration, du réseau, de la gestion des composants, des accès, des événements et de la disponibilité.

Ces correspondances sont **indicatives**. L'IEC 62443-2-1 décrit des exigences relatives au programme de sécurité du propriétaire d'actifs ; elle ne prescrit pas systématiquement un document portant le nom du livrable recensé.

Un rapprochement signifie donc qu'un livrable peut contribuer à démontrer ou mettre en œuvre une exigence. Il ne doit pas être interprété automatiquement comme une obligation de produire un document distinct.

---

## Comment utiliser ce catalogue ?

Le catalogue peut être utilisé à différentes étapes du cycle de vie d'un système industriel :

- **En cadrage**, pour identifier les productions à prévoir et répartir les responsabilités.
- **En conception**, pour relier les exigences de sécurité aux choix d'architecture et aux dossiers techniques.
- **En réalisation et qualification**, pour organiser les vérifications, essais et preuves.
- **Au transfert vers l'exploitation**, pour s'assurer que les informations nécessaires sont disponibles.
- **En exploitation**, pour maintenir les référentiels, tracer les changements, suivre les vulnérabilités et préparer les audits.

Il ne s'agit pas de produire systématiquement tous les documents de la liste. Le choix des livrables doit tenir compte du contexte industriel, de la criticité du système, des risques, des exigences réglementaires et contractuelles, ainsi que de l'organisation du projet et de l'exploitation.

L'enjeu est de disposer d'une documentation **utile, cohérente, maintenue à jour et proportionnée aux besoins**, plutôt que d'accumuler des documents sans propriétaire ni usage opérationnel.

---

## Périmètre et limites

Le catalogue est construit à partir de sources primaires et de référentiels identifiés dans le fichier Excel. Les références et les justifications sont précisées ligne par ligne.

Certaines correspondances ou références restent signalées comme à vérifier ou à compléter. Elles ne doivent pas être considérées comme des exigences établies tant que le rattachement précis n'a pas été confirmé.

Les textes réglementaires et les référentiels évoluent. Il convient donc de vérifier leur version en vigueur, leur applicabilité et les éventuelles exigences contractuelles propres au projet avant de retenir un livrable comme obligatoire.

---

*Catalogue CyberRepères — version 2.4.*

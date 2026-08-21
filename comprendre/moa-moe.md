---
layout: default
title: "MOA et MOE : comprendre les rôles dans un projet"
description: "Comprendre les notions de maîtrise d'ouvrage et de maîtrise d'œuvre à travers l'exemple de la construction d'une maison."
category: "comprendre"
tags:
  - MOA
  - MOE
  - projet
  - sous-traitance
  - cybersécurité industrielle
date: 2026-08-19
revision: 2026-08-19
chapter: "Fondamentaux"
order: 10
---

# MOA et MOE : comprendre les rôles dans un projet

Dans un projet industriel, il est essentiel de savoir **qui exprime le besoin, qui conçoit la solution et qui la réalise**.

Les termes **MOA** et **MOE** permettent justement de distinguer ces responsabilités :

- **MOA** : Maîtrise d'Ouvrage
- **MOE** : Maîtrise d'Œuvre

Pour comprendre simplement ces notions, imaginons un projet que tout le monde connaît : **faire construire une maison**.

---

## Construire une maison

Imaginez une personne très occupée par son travail. Elle souhaite faire construire sa maison, mais elle n'a ni le temps ni toutes les compétences techniques nécessaires pour concevoir le projet, consulter les entreprises et suivre sa réalisation. Le futur propriétaire sait ce qu'il veut obtenir : Une maison adaptée à sa famille, à son terrain, à son budget et à ses besoins. Pour cette tache de représentation, de suivi il fait appel a un chef de chantier, un gars expérimenté qui à l'habitude.
Ce chef de chantier expérimenté c'est la **Maîtrise d'Ouvrage : la MOA**. Il prend les décisions, et représente le futur propriétaire, (ou l'exploitant dans le cadre d'un projet industriel.
Note : le chef de chantier vendu une prestation d'AMOA pour Assistance à la Maitrse d'Ouvrage
---

## La MOA : « Je sais ce que je veux »

La MOA porte le besoin et définit les objectifs du projet.
Dans notre exemple, le futur propriétaire va notamment définir :

- la localisation de la maison
- sa surface
- le nombre de pièces
- son niveau de confort
- ses contraintes
- son budget
- ses attentes
- ses délais.

Il ne va pas nécessairement réaliser lui-même les plans, les calculs de structure ou les études électriques.
Son rôle est avant tout de **définir ce qu'il veut obtenir**.

---

## Le Constructeur c'est la MOE

Notre chef de chantier MOA fait appel à un constructeur. Ensemble, ils vont préciser le projet.
Avant la réalisation, le constructeur peut notamment :
- écouter les besoins de la MOA
- proposer des solutions
- réaliser ou coordonner
- produire les plans
- prendre en compte les contraintes réglementaires
- aider la MOA à faire ses choix
Le chef de chantier reste le **maître d'ouvrage** : c'est son affaire, il prend les décisions (pour le compte du futur propriétaire) cela relèvent de la maîtrise d'ouvrage.

Aprés validation, la **MOE sais comment le réaliser**. C'est justement le domaine de la **Maîtrise d'Œuvre : la MOE** se met alors en ordre de marche pour :
- réaliser les études techniques
- dimensionner les ouvrages
- calculer les structures en béton
- définir les besoins en ferraillage
- concevoir les installations électriques
- définir les installations de plomberie
- préparer les documents techniques
- consulter les entreprises spécialisées
- coordonner les travaux
- vérifier la conformité de la réalisation

La MOE traduit le besoin de la MOA en **solutions techniques réalisables**.
---
## MOA et MOE en une phrase

> **La MOA exprime le besoin et porte le projet.**

> **La MOE conçoit la solution et organise sa réalisation.**

Cette formulation est volontairement simplifiée. Dans les projets réels, les responsabilités peuvent être réparties différemment selon les contrats, les organisations et les missions confiées aux différents acteurs.

---

## Et les sous-traitants ?

Notre entreprise de construction ne va pas nécessairement réaliser elle-même tous les travaux.
Elle peut préparer des cahiers des charges et consulter des entreprises spécialisées :
- un terrassier
- un maçon
- un électricien
- un plombier
- un chauffagiste
- un spécialiste de la ventilation
- etc.

Ces entreprises peuvent alors intervenir comme **sous-traitants**.

```text
                    MOA
                     │
                     ▼
                    MOE
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
      Terrassier    Maçon    Électricien
      sous-traitant sous-traitant sous-traitant
```

## Et si plusieurs entreprises s'associent ?

Une entreprise peut ne pas disposer seule de toutes les compétences nécessaires pour répondre à un appel d'offres. Plusieurs entreprises peuvent alors décider de répondre ensemble. Elles forment un **groupement d'entreprises**. Les entreprises qui composent le groupement sont des **co-traitants**.

### Revenons à notre maison

Imaginons que le terrassier et le maçon décident de répondre ensemble au marché.
Ils peuvent alors devenir co-traitants plutôt que d'organiser la relation comme une sous-traitance du maçon vers le terrassier.

```text
                    MOE
                     │
             ┌───────┴───────┐
             │               │
          Maçon          Terrassier
             │               │
             └── Co-traitants
```

Cette organisation permet notamment d'éviter certaines chaînes de sous-traitance successives.

---

## Pourquoi cette distinction est-elle importante en cybersécurité industrielle ?

Dans un projet industriel, le nombre d'acteurs peut rapidement devenir important.
On peut retrouver :

```text
                         MOA
                          │
                          ▼
                         MOE
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        Intégrateur    Fournisseur   Entreprise
             │                         │
             ▼                         ▼
        Sous-traitant             Sous-traitant
```

Chaque niveau supplémentaire peut introduire :

- de nouveaux acteurs ;
- de nouveaux accès au système ;
- de nouvelles interfaces ;
- de nouvelles responsabilités ;
- de nouveaux risques ;
- de nouvelles dépendances.
La maîtrise de la chaîne de sous-traitance devient donc un **enjeu de cybersécurité**.

---

## Le lien avec le cycle en V
Dans les projets industriels, les responsabilités des différents acteurs peuvent être représentées au travers du **cycle en V**.
Le cycle en V permet notamment de représenter la progression d'un projet :

```text
Besoin
  │
  ▼
Exigences
  │
  ▼
Architecture
  │
  ▼
Conception
  │
  ▼
Réalisation
  │
  ▼
Intégration
  │
  ▼
Vérification
  │
  ▼
Validation
```

Le **CLUSIF**, dans son *Guide de la cybersécurité des systèmes industriels*, utilise notamment cette approche pour présenter le cycle en V et les missions des différents intervenants.

---

## Pourquoi la cybersécurité doit suivre le projet

La cybersécurité ne peut pas être ajoutée uniquement à la fin d'un projet.
Une expression de besoin comme : « Je veux un système industriel disponible et sécurisé. »
doit progressivement être traduite en :

```text
Besoin
   ↓
Exigences de sécurité
   ↓
Architecture de sécurité
   ↓
Spécifications
   ↓
Choix des équipements
   ↓
Configuration
   ↓
Tests
   ↓
Preuves
   ↓
Validation
```

La cybersécurité devient ainsi une caractéristique du système à construire, et non simplement une série de contrôles réalisés à la fin du projet.

---

## À retenir

| Acteur | Rôle simplifié |
|---|---|
| **MOA** | Porte le besoin et les objectifs du projet |
| **MOE** | Conçoit la solution et organise sa réalisation |
| **Fournisseur** | Fournit un produit ou une prestation |
| **Sous-traitant** | Réalise une partie de la prestation pour le compte d'un contractant |
| **Co-traitant** | Participe à un groupement d'entreprises répondant ensemble au marché |

La frontière exacte entre ces rôles dépend toutefois de l'organisation du projet, des contrats et des missions confiées à chaque acteur.

<!----- 

## Pour aller plus loin -->

<!--- [Cycle de vie d'un projet industriel](../methodes/cycle-de-v.md)-->
<!--- [Cycle en V](../methodes/cycle-en-v.md)-->
<!--- [Exigences de cybersécurité](../livrables/exigences-securite.md)-->
<!--- [Plan d'Assurance Sécurité](../livrables/plan-assurance-securite.md)-->
<!--- [Gestion de la chaîne d'approvisionnement](../pratiques/chaine-approvisionnement.md)-->
<!--- [IEC 62443](../referentiels/iec-62443.md)-->

---

**CyberRepères**

*Des références pour comprendre, des repères pour agir.*

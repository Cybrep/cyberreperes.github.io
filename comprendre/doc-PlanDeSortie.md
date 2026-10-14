---
layout: default
title: "Maîtrise des dépendances aux tiers et stratégies de sortie"
description: "le Plan de sortie c'est quoi ? son but ? comment s'y prendre ?..."
category: "comprendre"
tags:
  - TPRM
  - Plan de sortie
  - ICS
  - dépendances
  - Gestions des tiers
  - cybersécurité industrielle
  - Gouvernance
date: 2026-10-21
revision: 2026-10-21
chapter: "Documentation"
order: 40
comments: true
---


# Maîtriser les dépendances : anticiper pour ne pas subir

La gestion des dépendances peut vite devenir un casse-tête, particulièrement dans le monde industriel. Les investissements dans les outils de production sont importants, les équipements ont une longue durée de vie et les choix technologiques effectués aujourd'hui peuvent avoir des conséquences pendant plusieurs décennies. Changer de fournisseur, remplacer un équipement ou faire évoluer une solution propriétaire peut alors s'avérer complexe, coûteux, voire risqué pour la continuité de production.

Pour évaluer les conséquences d'une interruption sur l'activité, il existe notamment le BIA (Business Impact Analysis). Cette analyse mérite un article à part entière : elle permet d'identifier les impacts d'une interruption et de contribuer à définir les priorités de continuité.
Mais ce n'est pas le sujet du jour.

Nous allons nous intéresser à un autre aspect de la maîtrise des risques : la gestion des dépendances aux tiers, ou TPRM (Third-Party Risk Management).

Plus précisément, nous allons aborder un outil qui permet d'anticiper la fin d'une relation avec un fournisseur, le remplacement d'une solution ou la nécessité de reprendre une activité en interne : le plan de sortie (Exit Plan).

L'objectif n'est pas de chercher à supprimer toutes les dépendances, ce qui serait rarement réaliste, mais de comprendre celles que l'on accepte et de conserver une capacité d'action lorsqu'elles deviennent problématiques.


## 1. Comprendre les dépendances aux tiers

### 1.1. Qu'est-ce qu'une dépendance à un tiers ?

Une dépendance à un tiers existe lorsqu'une organisation s'appuie sur un acteur externe pour disposer d'une ressource, d'une technologie, d'un service ou d'une compétence nécessaire à son fonctionnement.

Dans le domaine informatique, ces dépendances sont souvent associées aux fournisseurs de services, aux éditeurs de logiciels ou aux prestataires. Mais elles ne se limitent pas à ces activités : elles concernent également les systèmes industriels, où les constructeurs, les intégrateurs et les mainteneurs jouent un rôle essentiel tout au long du cycle de vie des installations.

Une dépendance peut être à la fois une force et un risque. Elle permet de bénéficier de l'expertise d'un tiers, de compétences spécialisées ou de technologies que l'organisation ne pourrait pas développer en interne aussi rapidement, voire pas du tout.

Cependant, cette dépendance peut devenir problématique lorsqu'elle est difficile à maîtriser, à remplacer ou à contourner, notamment lorsque l'organisation ne dispose plus des ressources nécessaires pour poursuivre son activité sans le tiers concerné.

L'enjeu n'est donc pas de supprimer toutes les dépendances, mais de comprendre leur nature, leurs conséquences et les moyens de les maîtriser.

### 1.2. Quelles formes peuvent prendre les dépendances ?

Les dépendances aux tiers peuvent prendre plusieurs formes, qui se cumulent fréquemment.

- **Dépendance technologique :** l'utilisation d'une technologie propriétaire, d'un format fermé ou d'un protocole spécifique rend difficile le remplacement d'une solution.
- **Dépendance contractuelle :** les conditions de licence, les droits d'utilisation, les clauses de maintenance ou les modalités de transfert limitent les possibilités de changement.
- **Dépendance opérationnelle :** l'exploitation ou la maintenance d'un système nécessite l'intervention régulière d'un prestataire externe.
- **Dépendance humaine et documentaire :** les compétences, les connaissances historiques, les programmes sources ou la documentation indispensable sont détenus par un nombre restreint d'acteurs.
- **Dépendance matérielle :** le fonctionnement d'une installation repose sur des équipements, des pièces détachées ou des composants dont la disponibilité dépend d'un fournisseur.
- **Dépendance logicielle :** une solution nécessite des versions spécifiques d'un système d'exploitation, des bibliothèques, des licences ou des outils d'ingénierie qui ne peuvent pas facilement être remplacés.

Ces catégories ne sont pas exclusives. Un système industriel peut, par exemple, dépendre simultanément d'un constructeur pour les pièces détachées, d'un intégrateur pour les modifications applicatives et d'un éditeur pour les licences nécessaires pour la faire fonctionner.

### 1.3. Pourquoi ces dépendances sont-elles particulièrement importantes en OT ?

Dans un système d'information industriel (SII), les dépendances doivent être appréciées au regard des contraintes propres à l'outil de production.

Plusieurs caractéristiques expliquent cette particularité :

- **Des durées de vie longues :** les équipements industriels peuvent rester en service pendant plusieurs décennies, alors que les produits, les logiciels et les compétences nécessaires à leur maintenance évoluent ou disparaissent.
- **Des coûts de remplacement élevés :** changer plusieurs Automates (API) peut nécessiter des investissements importants, mais aussi des études, des essais, des arrêts programmés et des opérations de requalification.
- **Des contraintes de disponibilité :** une migration ne peut pas toujours être réalisée librement. Elle doit tenir compte des cycles de production, des fenêtres d'intervention et des exigences de continuité.
- **Des enjeux de sûreté et de sécurité :** la modification d'un automate, d'une supervision ou d'une architecture réseau peut affecter des fonctions essentielles. Toute évolution doit être évaluée et validée selon les exigences applicables au système concerné.
- **Des compétences spécialisées :** certains environnements nécessitent des outils propriétaires et une expertise difficile à acquérir ou à maintenir en interne.

Ainsi, une solution techniquement remplaçable peut cesser de l'être dès que l'on intègre le coût, le délai, la disponibilité et la maîtrise des risques.

### 1.4. Dépendance, Vendor lock-in et réversibilité : quelles différences ?

Ces trois notions sont liées, mais ne doivent pas être confondues.

**La dépendance à un tiers** désigne la situation dans laquelle une organisation s'appuie sur un acteur externe pour une ressource ou une capacité.

**Vendor Lock-in** désigne une situation dans laquelle les coûts, les contraintes techniques ou les obstacles contractuels rendent le changement de fournisseur particulièrement difficile.

**La réversibilité (*reversibility*)** désigne la capacité à reprendre un service, à transférer une activité ou à migrer vers une autre solution dans des conditions maîtrisées.

La stratégie de sortie (*exit strategy*) définit l'approche retenue pour mettre fin à une dépendance ou remplacer une solution. Le plan de sortie (*exit plan*) traduit cette stratégie en dispositions concrètes : responsabilités, prérequis, moyens, étapes, délais et conditions de réussite.

Une dépendance peut donc exister sans verrouillage important. À l'inverse, une organisation peut être fortement verrouillée alors même qu'elle dispose d'un contrat prévoyant formellement la réversibilité.

### 1.5. Exemple industriel : une supervision propriétaire

Prenons l'exemple d'une installation dont la supervision (SCADA) repose sur une solution propriétaire, développée et maintenue par un intégrateur.

L'exploitant dispose des licences nécessaires à l'utilisation du système, mais les fichiers sources, certains outils d'ingénierie et une partie des connaissances nécessaires à la maintenance sont détenus par le prestataire.

Tant que la relation contractuelle fonctionne, cette organisation peut être parfaitement opérationnelle. Mais que se passerait-il si le prestataire cessait son activité, si le contrat n'était pas renouvelé ou si les conditions commerciales devenaient inacceptables ?

**Quelles données et quels éléments l'exploitant serait-il en mesure de récupérer ? Et surtout, seraient-ils réellement exploitables ?**

La récupération d'une sauvegarde de la supervision ne garantit pas, à elle seule, la possibilité de reprendre son exploitation ou de la faire évoluer. Plusieurs questions se posent alors :

- Les programmes, les configurations et les fichiers nécessaires à la reconstruction du système sont-ils disponibles ?
- Les formats utilisés sont-ils documentés et exploitables sans l'intervention du fournisseur initial ?
- Les licences et les outils d'ingénierie nécessaires sont-ils disponibles et utilisables dans la durée ?
- Les versions des logiciels, leurs dépendances et les environnements nécessaires à leur fonctionnement sont-ils connus ?
- La documentation permet-elle à un autre intégrateur de comprendre l'architecture et de reprendre la maintenance ?
- Les sauvegardes ont-elles été vérifiées et leur restauration a-t-elle été testée ?

Ces questions dépassent la simple possession des données. Elles portent sur la capacité réelle à les exploiter, à reconstruire le système, à le maintenir et, si nécessaire, à le migrer vers une autre solution.

Une organisation peut ainsi disposer de sauvegardes complètes sans être capable de restaurer la supervision dans un environnement opérationnel. De même, récupérer les programmes sources ne garantit pas qu'un autre prestataire pourra les modifier sans disposer des outils, des licences et des connaissances nécessaires.

Cet exemple illustre un principe essentiel : **la capacité à récupérer des données ou des fichiers ne garantit pas la capacité à reprendre le contrôle du système.**

Anticiper les conditions de sortie consiste donc aussi à vérifier, avant qu'une rupture ne survienne, que les éléments récupérables sont effectivement exploitables et qu'une reprise par un autre acteur est techniquement envisageable.

## 2. Pourquoi anticiper une sortie ?

### 2.1. Préparer le divorce le jour du mariage

Personne n'a envie de parler de divorce le jour de son mariage. Pourtant, c'est précisément à ce moment-là que les deux parties disposent de la plus grande liberté pour définir les conditions de leur engagement.

Dans une relation commerciale, le raisonnement est similaire. Lorsqu'un fournisseur est sélectionné, que le contrat est en cours de négociation et que le projet n'a pas encore démarré, il est encore possible de discuter des conditions de sortie : récupération des données, transfert des compétences, restitution des configurations, accès aux programmes sources, maintien des licences ou assistance à la transition.

Une fois le contrat signé, la solution déployée et les équipes devenues dépendantes du fournisseur, le rapport de force peut changer. Renégocier certaines conditions devient plus difficile, et les coûts d'un changement peuvent rapidement devenir prohibitifs.

**Le meilleur moment pour négocier les conditions de sortie est donc souvent celui où personne n'envisage encore de partir.**

Cette anticipation ne traduit pas un manque de confiance envers le fournisseur. Elle relève d'une démarche de bonne gestion : une relation peut être satisfaisante aujourd'hui sans que sa continuité soit garantie pour toute la durée de vie du système.

### 2.2. Une relation peut prendre fin pour de nombreuses raisons

La fin d'une relation avec un tiers n'est pas nécessairement la conséquence d'un conflit. Plusieurs situations peuvent conduire à envisager une sortie :

- **Fin de vie technologique :** le fournisseur arrête la commercialisation ou le support d'un produit.
- **Évolution contractuelle :** les coûts augmentent, les licences changent ou les conditions de maintenance deviennent moins favorables.
- **Disparition ou défaillance du fournisseur :** l'entreprise cesse son activité, est rachetée ou ne dispose plus des compétences nécessaires.
- **Évolution stratégique :** l'organisation souhaite internaliser une activité, rationaliser son parc ou changer de technologie.
- **Incident de cybersécurité :** une compromission, une perte de confiance ou une incapacité à corriger des vulnérabilités conduit à reconsidérer la relation.
- **Contraintes opérationnelles :** les délais d'intervention, la disponibilité des pièces ou la qualité du service ne répondent plus aux besoins.

Dans l'industrie, ces événements peuvent se produire alors que les équipements restent parfaitement fonctionnels. La fin du support d'un automate, par exemple, ne signifie pas qu'il doit être remplacé immédiatement. Elle peut néanmoins rendre nécessaire la préparation d'une stratégie de maintien en condition opérationnelle ou de remplacement.

### 2.3. Anticiper avant de perdre sa capacité d'action

Une sortie devient particulièrement difficile lorsque l'organisation découvre, au moment où elle en a besoin, qu'elle ne dispose pas des moyens nécessaires pour la réaliser.

Les difficultés peuvent être très concrètes :

- les programmes sources ou les configurations ne sont pas accessibles ;
- les licences ne sont pas transférables ;
- les données ne peuvent pas être exportées dans un format exploitable ;
- les connaissances techniques sont concentrées chez un seul prestataire ;
- aucune solution de remplacement n'a été étudiée ;
- les délais de migration sont incompatibles avec les contraintes de production ;
- le budget nécessaire n'a pas été anticipé.

Ces obstacles ne peuvent pas tous être éliminés par une clause contractuelle. Certains nécessitent des choix d'architecture, la conservation de compétences, des essais techniques ou la préparation d'un remplacement sur plusieurs années.

L'objectif est donc de préserver une capacité de décision et d'action avant que l'urgence ne s'impose.

### 2.4. Anticiper ne signifie pas nécessairement sortir

Préparer un plan de sortie ne signifie pas que la sortie est souhaitable ou qu'elle doit être déclenchée au premier problème.

Dans certains cas, conserver la solution existante demeure le meilleur choix, notamment lorsque le remplacement présente des risques industriels importants ou nécessite des investissements disproportionnés.

Le plan permet alors de connaître les options disponibles, les prérequis à réunir, les délais nécessaires et les conséquences d'une décision. Il constitue un outil d'aide à la décision, mais aussi un moyen de réduire les situations dans lesquelles l'organisation se retrouve sans alternative réaliste.

**L'enjeu n'est pas de prévoir systématiquement le départ, mais d'éviter de se retrouver dans l'impossibilité de partir.**

## 3. Identifier et évaluer les dépendances

### 3.1. Identifier les dépendances avant qu'elles ne deviennent des contraintes

La maîtrise des dépendances commence par une question simple : de quoi dépend réellement notre capacité à exploiter, maintenir et faire évoluer le système ?

La réponse ne se limite pas à la liste des fournisseurs et des contrats. Une organisation peut être dépendante d'un constructeur pour ses pièces détachées, d'un éditeur pour ses licences, d'un intégrateur pour les modifications ou d'un prestataire pour des compétences qu'elle ne possède pas en interne.

Dans un système d'information industriel (SII), il est notamment nécessaire d'examiner :

- **Les équipements et technologies :** automates, systèmes de supervision, réseaux industriels, capteurs, protocoles propriétaires et composants spécifiques.
- **Les logiciels et licences :** outils d'ingénierie, environnements de développement, systèmes d'exploitation, logiciels de supervision et mécanismes de licence.
- **Les compétences et connaissances :** expertise du constructeur, maîtrise des programmes applicatifs, connaissance de l'architecture et capacité à diagnostiquer les incidents.
- **Les données et la documentation :** programmes sources, configurations, schémas, dossiers d'exploitation, procédures de maintenance et historiques.
- **Les prestations et services :** maintenance, assistance technique, mises à jour, support constructeur et interventions spécialisées.
- **Les approvisionnements :** pièces détachées, composants de remplacement et disponibilité des équipements sur la durée.

Ces dépendances doivent être examinées à l'échelle du système, et pas uniquement fournisseur par fournisseur. Un équipement peut sembler facilement remplaçable pris isolément, mais être fortement lié à d'autres composants par ses interfaces, ses outils d'ingénierie ou les choix d'architecture réalisés lors de son intégration.

L'objectif est donc de comprendre les liens entre les composants, les acteurs et les compétences nécessaires au fonctionnement de l'ensemble.

### 3.2. Le rôle de la MOE : rendre les dépendances visibles

Dans un projet industriel, la maîtrise des dépendances ne relève pas uniquement des achats, des contrats ou de la cybersécurité. Elle nécessite également une compréhension approfondie des choix techniques et de leurs conséquences.

C'est ici que la maîtrise d'œuvre (MOE) joue un rôle important.

La MOA exprime le besoin, définit les objectifs du projet et porte les arbitrages relevant de son périmètre. La MOE traduit ce besoin en solutions techniques, contribue aux choix d'architecture et organise la conception, l'intégration et la vérification du système.

À ce titre, la MOE est particulièrement bien placée pour identifier les dépendances qui résultent des choix techniques qu'elle fait et en expliquer les conséquences à sa MOA.

Son rôle consiste notamment à :

- **Identifier les dépendances techniques** induites par les architectures, les équipements, les logiciels et les solutions retenues.
- **Analyser les conséquences des choix technologiques**, notamment en matière de compatibilité, de maintenabilité, d'évolutivité et de remplacement.
- **Évaluer les contraintes d'intégration** entre les équipements, les systèmes existants et les solutions fournies par différents acteurs.
- **Vérifier les conditions de reprise**, par exemple l'accès aux programmes sources, aux configurations, aux outils d'ingénierie et à la documentation nécessaire.
- **Proposer des alternatives techniques** lorsque plusieurs solutions permettent de répondre au besoin, en explicitant leurs avantages, leurs limites et les dépendances associées.
- **Alerter sur les risques identifiés** et fournir les éléments nécessaires aux arbitrages de la MOA.

Cette contribution est essentielle dès la conception. Une dépendance difficile à maîtriser peut résulter d'un choix effectué très tôt dans le projet, alors que les marges de manœuvre sont encore importantes.

À l'inverse, découvrir en phase d'exploitation qu'un équipement ne peut être maintenu ou remplacé sans l'intervention exclusive d'un fournisseur peut conduire à des opérations coûteuses et à des délais difficiles à maîtriser.

La décision d'accepter une dépendance ne repose pas sur la seule MOE. Elle doit en revanche contribuer à ce que cette décision soit prise en connaissance de cause.

### 3.3. Évaluer la criticité des dépendances

Toutes les dépendances n'ont pas le même niveau de criticité. Une organisation peut accepter une dépendance forte à une technologie spécialisée si les conséquences sont maîtrisées et si aucune alternative raisonnable n'existe.

L'évaluation doit donc dépasser le simple constat de dépendance pour examiner les conséquences d'une rupture et la capacité de l'organisation à y faire face.

Plusieurs critères peuvent être utilisés :

| Critère | Questions à se poser |
|---|---|
| Criticité opérationnelle | Que se passe-t-il si le fournisseur ne peut plus intervenir ou si le composant devient indisponible ? |
| Substituabilité | Existe-t-il une solution alternative compatible avec le système existant ? |
| Maîtrise technique | Dispose-t-on des sources, configurations, licences, documentations et compétences nécessaires ? |
| Délai de remplacement | Combien de temps faudrait-il pour migrer, remplacer ou reprendre l'activité ? |
| Impact économique | Quels seraient les coûts de transition, de développement, d'essais et d'arrêt de production ? |
| Risques industriels | La modification peut-elle affecter la disponibilité, l'intégrité du contrôle-commande ou des fonctions de sécurité ? |
| Dépendance contractuelle | Les droits, les licences et les engagements du fournisseur permettent-ils d'envisager une transition réaliste ? |

Ces critères doivent être adaptés à la nature du système et à ses enjeux. Dans certains environnements industriels, le délai nécessaire pour qualifier une solution de remplacement sera plus déterminant que son coût d'acquisition.

L'évaluation peut s'appuyer sur l'analyse de risques et, lorsque cela est pertinent, sur le BIA (*Business Impact Analysis*) afin de mieux comprendre les conséquences d'une interruption sur l'activité.

Inutile de viser un score unique : l'essentiel est de disposer d'une analyse argumentée qui permette de distinguer les dépendances acceptables, celles qui nécessitent des mesures de maîtrise et celles pour lesquelles une stratégie de sortie doit être préparée.

### 3.4. De l'analyse technique à la décision

Une fois les dépendances identifiées et évaluées, les résultats doivent être partagés avec les acteurs qui portent les décisions.

La MOE apporte sa connaissance technique du système, explicite les contraintes et présente les solutions envisageables. La MOA, en lien avec les responsables concernés, peut alors arbitrer entre les coûts, les bénéfices, les contraintes d'exploitation et les risques acceptés.

Plusieurs décisions sont possibles :

- conserver la solution existante en acceptant la dépendance identifiée ;
- renforcer les garanties contractuelles et la documentation disponible ;
- améliorer l'autonomie de maintenance et les compétences internes ;
- prévoir des pièces de rechange ou des mesures compensatoires ;
- imposer des exigences de portabilité ou de réversibilité dans les marchés ;
- programmer le remplacement de la solution et préparer un plan de sortie.

Le résultat attendu n'est pas nécessairement une sortie immédiate. Il s'agit de transformer une dépendance parfois subie en une situation comprise, évaluée et assumée.

**Une dépendance maîtrisée est une dépendance dont les conséquences sont connues, dont les risques sont traités et pour laquelle les décisions sont prises en connaissance de cause.**

## 4. Définir la stratégie de sortie

### 4.1. Sortir de la dépendance : pour aller vers quoi ?

Identifier une dépendance et en évaluer la criticité ne suffit pas. Il faut ensuite déterminer quelle réponse apporter.

Une dépendance peut être acceptable dans la durée, à condition que les risques associés soient maîtrisés. Dans d'autres situations, il peut être nécessaire de réduire cette dépendance, de préparer un changement de fournisseur ou d'anticiper le remplacement d'une technologie.

La stratégie de sortie définit l'orientation retenue pour répondre à ces situations. Elle précise les objectifs recherchés, les scénarios envisageables et les conditions dans lesquelles une sortie pourrait être engagée.

Plusieurs stratégies sont possibles :

- **Changer de prestataire :** conserver la solution technique, mais transférer son exploitation ou sa maintenance à un autre acteur.
- **Reprendre l'activité en interne :** développer les compétences et acquérir les moyens nécessaires pour assurer soi-même certaines activités.
- **Remplacer la technologie :** migrer vers une solution alternative afin de réduire la dépendance à un constructeur, à un éditeur ou à une technologie propriétaire.
- **Réduire progressivement la dépendance :** préparer une migration par étapes, conserver temporairement l'existant et limiter les risques liés à une transition brutale.
- **Maintenir la solution existante :** lorsque le remplacement est disproportionné ou trop risqué, prolonger son utilisation tout en renforçant les mesures de maîtrise et en préparant les évolutions nécessaires.

Ces stratégies ne sont pas exclusives. Une organisation peut, par exemple, changer d'intégrateur tout en conservant son système de supervision, puis programmer le remplacement de celui-ci plusieurs années plus tard.

L'objectif n'est pas de choisir systématiquement la solution la plus indépendante, mais celle qui répond le mieux aux besoins de l'organisation compte tenu des risques, des contraintes et des ressources disponibles.

### 4.2. Déterminer les conditions de déclenchement

Une stratégie de sortie doit préciser dans quelles circonstances elle pourrait être mise en œuvre.

Sans critères préalablement définis, la décision risque d'être prise dans l'urgence, lorsque les marges de manœuvre sont déjà réduites.

Les conditions de déclenchement peuvent notamment être liées à :

- la fin du support constructeur ou à l'arrêt de la maintenance ;
- une augmentation importante des coûts ou une évolution défavorable des conditions contractuelles ;
- l'indisponibilité prolongée d'un fournisseur ou d'un prestataire ;
- l'apparition de vulnérabilités qui ne peuvent plus être corrigées dans des conditions acceptables ;
- l'impossibilité de satisfaire de nouvelles exigences techniques ou réglementaires ;
- une évolution de la stratégie industrielle ou de l'architecture cible ;
- une dégradation de la capacité à maintenir ou à faire évoluer le système.

Ces critères doivent être adaptés au contexte. La fin du support d'un équipement n'impose pas son remplacement immédiat. Elle peut toutefois constituer un événement déclenchant une réévaluation des risques et l'activation d'un scénario préalablement étudié.

Il convient également de distinguer les événements qui nécessitent une sortie immédiate de ceux qui permettent une transition planifiée. Dans un environnement industriel, une migration précipitée peut présenter davantage de risques que le maintien temporaire d'une solution existante, sous réserve de mesures compensatoires adaptées.

### 4.3. Comparer les scénarios et leurs conséquences

Plusieurs scénarios peuvent permettre de réduire une dépendance, mais ils n'impliquent ni les mêmes coûts ni les mêmes contraintes.

La comparaison doit prendre en compte les conséquences techniques, économiques, opérationnelles et organisationnelles de chaque option.

| Critère | Questions à examiner |
|---|---|
| Faisabilité technique | La solution cible est-elle compatible avec les équipements, les interfaces et les applications existantes ? |
| Continuité de production | Quelle indisponibilité sera nécessaire pour réaliser la transition ? |
| Sécurité industrielle | Quels essais et quelles validations seront nécessaires avant la mise en service ? |
| Cybersécurité | Le scénario permet-il de maintenir ou d'améliorer le niveau de sécurité attendu ? |
| Coût global | Quels sont les coûts d'étude, de migration, de qualification, de formation et de maintenance ? |
| Délai | Combien de temps faut-il pour préparer et mettre en œuvre la sortie ? |
| Autonomie future | La nouvelle solution réduit-elle réellement la dépendance ou la déplace-t-elle vers un autre acteur ? |
| Réversibilité | Sera-t-il plus facile de changer de fournisseur ou de solution à l'avenir ? |

Ce travail nécessite une contribution technique importante de la maîtrise d'œuvre (MOE). Elle peut étudier les scénarios, identifier les contraintes d'intégration, estimer les efforts de migration et préciser les conditions nécessaires à une transition maîtrisée.

La maîtrise d'ouvrage (MOA), en lien avec les responsables concernés, dispose alors d'éléments concrets pour arbitrer entre les différentes options.

Un point mérite une attention particulière : **changer de fournisseur ne fait pas disparaître la dépendance**. Une solution alternative peut présenter les mêmes contraintes, voire introduire de nouvelles dépendances. Il est donc important d'évaluer la situation cible et pas uniquement les difficultés de sortie de la situation actuelle.

### 4.4. Définir les prérequis de la stratégie retenue

Une stratégie de sortie ne peut être considérée comme réaliste que si les moyens nécessaires à sa mise en œuvre sont identifiés.

Selon le scénario retenu, plusieurs prérequis peuvent être nécessaires :

- disposer des programmes sources, des configurations et de la documentation ;
- vérifier les droits d'utilisation et de transfert des licences ;
- identifier les compétences internes ou les prestataires capables de reprendre l'activité ;
- s'assurer de la disponibilité des équipements et des outils nécessaires ;
- prévoir les essais, les validations et les éventuelles opérations de requalification ;
- réserver les budgets et les fenêtres d'intervention nécessaires ;
- identifier les dépendances qui subsisteront après la transition.

Certains prérequis peuvent être préparés contractuellement dès la sélection du fournisseur. D'autres relèvent de décisions d'architecture ou d'investissements à planifier sur plusieurs années.

C'est pourquoi la stratégie de sortie doit être envisagée suffisamment tôt dans le cycle de vie du système. Une disposition contractuelle ne compensera pas, à elle seule, l'absence de compétences, d'outils ou de solution technique de remplacement.

### 4.5. Formaliser la décision et préparer le plan de sortie

Une fois la stratégie retenue, elle doit être traduite en dispositions opérationnelles.

La décision doit préciser le scénario privilégié, les conditions de déclenchement, les principaux risques, les moyens nécessaires et les responsabilités associées. Elle doit également indiquer les mesures à prendre si la sortie ne peut pas être réalisée immédiatement.

Le plan de sortie détaillera ensuite les actions à mener, leur séquencement, les ressources mobilisées, les échéances et les critères permettant de vérifier que la transition est maîtrisée.

La stratégie et le plan de sortie sont donc complémentaires :

- **La stratégie de sortie** répond à la question : quelle orientation retenir et dans quelles circonstances ?
- **Le plan de sortie** répond à la question : comment mettre cette orientation en œuvre concrètement ?

Cette distinction permet d'éviter qu'un plan de sortie ne soit réduit à une procédure générique, déconnectée des choix techniques, des contraintes industrielles et des objectifs de l'organisation.

L'objectif final est de disposer d'une option réaliste et préparée, sans pour autant s'engager prématurément dans une migration qui ne serait ni nécessaire ni pertinente.

## 5. Construire le plan de sortie

### 5.1. Un document opérationnel, pas une simple clause contractuelle

Le plan de sortie traduit la stratégie retenue en dispositions concrètes permettant de mettre fin à une relation avec un tiers, de changer de fournisseur ou de remplacer une solution, tout en maîtrisant les conséquences de cette transition.

Il ne doit pas être confondu avec une clause de réversibilité insérée dans un contrat. Cette dernière peut définir certains droits et obligations du fournisseur, mais elle ne suffit pas à garantir que l'organisation dispose des moyens techniques, humains et financiers nécessaires à la sortie.

Un plan de sortie doit donc répondre à plusieurs questions :

- Dans quelles circonstances la sortie peut-elle être déclenchée ?
- Quel est le périmètre concerné et quel résultat cherche-t-on à atteindre ?
- Quelles ressources, données, configurations et compétences sont nécessaires ?
- Quelles étapes doivent être réalisées, et dans quel ordre ?
- Comment garantir la continuité de l'activité pendant la transition ?
- Comment vérifier que la solution cible est opérationnelle et maîtrisée ?

Le niveau de détail doit être proportionné à la criticité de la dépendance. Une prestation facilement substituable n'appelle pas le même dispositif qu'une supervision industrielle propriétaire ou qu'un système de contrôle-commande difficile à remplacer.

### 5.2. Définir le périmètre et les responsabilités

Le document doit commencer par identifier précisément la dépendance concernée.

Il convient notamment de préciser :

- le fournisseur, le prestataire ou la technologie concernés ;
- les contrats, services, équipements et systèmes inclus dans le périmètre ;
- les fonctions industrielles et les activités susceptibles d'être affectées ;
- les dépendances associées, notamment les logiciels, les licences, les interfaces et les sous-traitants ;
- les responsables du plan et les acteurs qui devront intervenir lors de sa mise en œuvre.

Les responsabilités doivent être explicites. La maîtrise d'ouvrage (MOA) porte les décisions relevant de son périmètre, tandis que la maîtrise d'œuvre (MOE) contribue à définir les modalités techniques de transition, à évaluer les contraintes et à vérifier la faisabilité des scénarios retenus.

Les achats, les services juridiques, les équipes d'exploitation, la maintenance et la cybersécurité doivent également être associés selon la nature de la dépendance.

Un plan de sortie ne peut pas reposer uniquement sur une équipe technique si les conditions contractuelles, les budgets ou les décisions d'exploitation conditionnent sa réalisation.

### 5.3. Garantir la récupération et l'exploitation des actifs

La récupération des éléments nécessaires à la reprise constitue souvent l'un des points les plus sensibles du plan de sortie.

Il ne suffit pas de prévoir une restitution des données. Il faut identifier les éléments nécessaires pour continuer à exploiter, maintenir, reconstruire ou migrer la solution.

Dans un contexte industriel, cette vérification peut porter sur :

- les données, historiques et fichiers d'export ;
- les programmes sources et les fichiers de configuration ;
- les sauvegardes des équipements et les procédures de restauration ;
- les schémas d'architecture, les plans de câblage et la documentation technique ;
- les versions logicielles, les dépendances et les outils d'ingénierie ;
- les licences, les clés d'activation et les droits d'utilisation ;
- les comptes techniques et les modalités de transfert des accès ;
- les procédures d'exploitation, de maintenance et de diagnostic.

Pour chaque élément, le plan doit préciser où il se trouve, qui en a la responsabilité, sous quel format il est disponible et dans quelles conditions il peut être récupéré et utilisé.

La question centrale reste celle de l'exploitabilité. Un fichier récupéré dans un format propriétaire, sans outil compatible ou sans licence valide, peut ne présenter qu'une valeur opérationnelle limitée.

Lorsque les enjeux le justifient, il est donc nécessaire de vérifier que les éléments récupérés permettent effectivement de restaurer le système, de reprendre la maintenance ou d'engager une migration.

### 5.4. Définir le scénario de transition

Le plan doit décrire la manière dont la sortie sera réalisée.

Selon la stratégie retenue, il peut s'agir d'un transfert vers un nouveau prestataire, d'une reprise en interne, d'une migration technique ou d'un remplacement progressif de la solution.

Le scénario doit notamment préciser :

- la solution cible et les conditions nécessaires à sa mise en œuvre ;
- les étapes de préparation, de transfert et de transition ;
- les ressources humaines et techniques à mobiliser ;
- les compétences à acquérir ou à transférer ;
- les dépendances qui devront être levées avant chaque étape ;
- les contraintes de calendrier et les fenêtres d'intervention ;
- les risques associés à la transition et les mesures de réduction correspondantes.

En OT, le scénario doit également tenir compte des contraintes de production et des exigences applicables en matière de sûreté, de sécurité industrielle et de cybersécurité.

Le remplacement d'une supervision ou d'un automate ne peut pas être traité comme une simple migration informatique. Il peut nécessiter des essais d'intégration, des vérifications fonctionnelles, la validation des interfaces et une mise en service contrôlée.

Le plan doit donc prévoir les conditions permettant de vérifier que la solution cible répond aux exigences attendues avant que l'ancienne solution ne soit définitivement abandonnée.

### 5.5. Préserver la continuité de production

La transition doit être organisée de manière à limiter les conséquences sur l'activité industrielle.

Selon le système concerné, plusieurs mesures peuvent être nécessaires :

- prévoir une transition pendant un arrêt programmé ;
- maintenir temporairement l'ancien système en fonctionnement ;
- organiser une migration progressive par zones ou sous-systèmes ;
- disposer d'une solution de repli en cas d'échec ;
- prévoir les moyens de restauration et de retour à une configuration connue ;
- définir les conditions de validation avant la remise en exploitation.

Le plan doit préciser les conditions dans lesquelles la transition peut être poursuivie, suspendue ou annulée.

Il doit également tenir compte du fait que le retour arrière n'est pas toujours possible. Certaines modifications peuvent être irréversibles, ou rendre nécessaire une nouvelle séquence de validation avant de revenir à la configuration précédente.

La continuité ne doit donc pas être considérée comme une conséquence automatique de la préparation du plan. Elle doit être intégrée au scénario et vérifiée au regard des contraintes réelles de l'installation.

### 5.6. Prévoir les moyens, les délais et le financement

Un scénario de sortie n'est crédible que si les ressources nécessaires sont identifiées.

Le plan doit estimer les coûts associés à la préparation et à la réalisation de la transition : prestations, licences, équipements, études, développement, essais, formation, arrêt de production et éventuelle période de fonctionnement en parallèle.

Il doit également préciser les compétences nécessaires, les responsables des actions et les délais prévisionnels.

Dans l'industrie, le délai constitue souvent une contrainte majeure. Même lorsqu'une solution de remplacement existe, son intégration et sa validation peuvent nécessiter plusieurs mois, voire davantage selon la criticité et la complexité du système.

Ces éléments doivent permettre à l'organisation d'identifier les prérequis à financer ou à préparer avant qu'une sortie ne devienne urgente.

### 5.7. Définir les critères de réussite

Le plan doit enfin préciser comment vérifier que la sortie est effectivement achevée.

La fin du contrat avec le fournisseur ne suffit pas à supprimer la dépendance. Certaines licences, certains composants ou certaines compétences peuvent rester liés à l'ancien acteur.

Les critères de réussite peuvent notamment porter sur :

- la récupération et la validation des actifs nécessaires ;
- le fonctionnement opérationnel de la solution cible ;
- la disponibilité des compétences et des moyens de maintenance ;
- la conformité des configurations et des accès ;
- la réalisation des essais et validations prévus ;
- la continuité des activités et la levée des risques identifiés ;
- le traitement des accès, données et informations restant chez l'ancien prestataire ;
- la documentation de la nouvelle situation et des dépendances résiduelles.

La sortie doit être considérée comme achevée lorsque les objectifs définis ont été atteints et que l'organisation dispose des moyens nécessaires pour poursuivre son activité dans les conditions attendues.

Un bilan doit également permettre d'identifier les difficultés rencontrées et les améliorations à apporter aux futurs plans de sortie.

## 6. Maintenir le plan et vérifier sa faisabilité

Un plan de sortie est comparable à une carte que l'on consulte en pleine tempête. Si elle est obsolète, incomplète ou imprécise, elle risque de nous conduire dans la mauvaise direction au moment où nous en avons le plus besoin.

Un plan de sortie ne doit donc pas être considéré comme un document que l'on rédige une fois pour répondre à une exigence, puis que l'on range dans un répertoire. Il doit rester cohérent avec la réalité du système, les conditions contractuelles et les moyens dont dispose l'organisation.

Sa mise à jour doit notamment être envisagée lors d'un changement de fournisseur, d'architecture, de licence, de version logicielle, de contrat ou de conditions de maintenance. Une évolution importante des compétences disponibles ou de la solution de remplacement peut également remettre en cause le scénario initial.

Mais maintenir le document à jour ne suffit pas. Encore faut-il vérifier que le plan reste applicable.

Les éléments nécessaires à la sortie sont-ils toujours accessibles ? Les licences sont-elles valides et transférables ? Les sauvegardes sont-elles exploitables ? Les compétences et les ressources nécessaires sont-elles disponibles ? Les délais prévus restent-ils compatibles avec les contraintes de production ?

Selon la criticité de la dépendance, ces vérifications peuvent prendre la forme d'une revue documentaire, d'un contrôle des prérequis ou d'un exercice permettant de tester certains aspects du scénario, sans perturber l'exploitation.

**Une carte que l'on n'a jamais vérifiée peut donner une illusion de sécurité. Un plan de sortie que l'on n'a jamais éprouvé présente le même risque.**

L'objectif n'est pas de tester systématiquement une sortie complète, parfois irréaliste ou dangereuse en environnement industriel, mais de s'assurer que les hypothèses du plan restent valides et que les moyens nécessaires seront disponibles le jour où il faudra l'activer.

## 7. Références et littérature de référence

La maîtrise des dépendances aux tiers et la préparation d'un plan de sortie s'appuient sur plusieurs référentiels relatifs à la cybersécurité, à la gestion des fournisseurs et à la continuité des activités.

Il n'existe pas un référentiel unique définissant un modèle universel de plan de sortie applicable à tous les systèmes industriels. Les références ci-dessous apportent des principes et des recommandations permettant de construire une démarche adaptée aux enjeux du système et aux contraintes de l'organisation.

### 7.1. Normes et référentiels

#### ISO/IEC 27036 — Cybersécurité et relations avec les fournisseurs

La série ISO/IEC 27036 traite de la sécurité des relations entre fournisseurs et clients. Elle constitue une référence pour intégrer les exigences de cybersécurité dans les relations contractuelles et la gestion des risques liés aux tiers.

Les différentes parties abordent notamment les concepts généraux, les exigences relatives aux relations avec les fournisseurs et les risques liés à la chaîne d'approvisionnement des produits et services TIC.

Cette série peut servir de cadre général pour identifier les dépendances, définir les exigences applicables aux fournisseurs et anticiper les conditions de fin de relation.

- [ISO/IEC 27036-1:2021 Cybersécurité — Relations avec le fournisseur Partie 1: Aperçu général et concepts](https://www.iso.org/fr/standard/82905.html)
- [ISO/IEC 27036-2:2022 Cybersecurity - Supplier relationships - Part 2: Requirements](https://www.boutique.afnor.org/fr-fr/norme/iso-iec-2703622022/xs139993/326466)
- [ISO/IEC 27036-3 Cybersécurité - Relations avec le fournisseur - Partie 3: Lignes directrices pour la sécurité de la chaîne de fourniture en matériel, logiciels et services](https://www.boutique.afnor.org/fr-fr/norme/iso-iec-2703632023/cybersecurite-relations-avec-le-fournisseur-partie-3-lignes-directrices-pou/xs141357/346844)

#### IEC 62443-2-1 — Programme de cybersécurité de l'exploitant industriel

La norme IEC 62443-2-1 définit des exigences relatives au programme de cybersécurité des propriétaires et exploitants de systèmes d'automatisation et de contrôle industriels (IACS).

Elle permet de replacer la maîtrise des dépendances dans une démarche globale de gestion de la cybersécurité, en tenant compte des contraintes d'exploitation, de maintenance et du cycle de vie des installations industrielles.

- [IEC 62443-2-1:2024 — Sécurité des systèmes d’automatisation et de commande industrielles - Partie 2-1: Exigences de programme de sécurité pour les propriétaires d’actif IACS](https://www.boutique.afnor.org/fr-fr/norme/iec-62443212024/securite-des-systemes-dautomatisation-et-de-commande-industrielles-partie-2/xs300589/431169)

#### IEC 62443-2-4 — Exigences applicables aux prestataires de services industriels

La norme IEC 62443-2-4 porte sur les capacités de cybersécurité des prestataires intervenant dans l'intégration et la maintenance des systèmes d'automatisation et de contrôle industriels.

Elle complète la perspective de l'exploitant en apportant un cadre pour examiner les pratiques de sécurité des intégrateurs et des prestataires de maintenance.

- [IEC 62443-2-4:2024 — Sécurité des automatismes industriels et des systèmes de commande - Partie 2-4 : exigences de programme de sécurité pour les fournisseurs de service IACS](https://www.boutique.afnor.org/fr-fr/norme/nf-en-iec-6244324/securite-des-automatismes-industriels-et-des-systemes-de-commande-partie-24/fa201630/414312)

### 7.2. Guides pratiques et publications

#### ANSSI — Externalisation et sécurité des systèmes d'information

Ce guide aborde les risques liés à l'externalisation et les mesures permettant de conserver la maîtrise des systèmes d'information confiés à des prestataires.

Il constitue une ressource francophone utile pour approfondir les enjeux contractuels, organisationnels et techniques de la relation fournisseur. Son contenu est principalement orienté vers les systèmes d'information classiques : son application à l'OT doit donc tenir compte des contraintes industrielles propres aux installations concernées.

- [ANSSI — Externalisation et sécurité des systèmes d'information : un guide pour maîtriser les risques](https://messervices.cyber.gouv.fr/guides/externalisation-et-securite-des-systemes-dinformation-un-guide-pour-maitriser-les)

#### NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations

Cette publication du NIST propose une démarche de gestion des risques de cybersécurité liés à la chaîne d'approvisionnement. Elle traite notamment de l'identification, de l'évaluation et du traitement des risques associés aux produits et services tout au long de leur cycle de vie.

Elle constitue une ressource complémentaire pour structurer l'analyse des dépendances et leur prise en compte dans la gouvernance des risques.

- [NIST SP 800-161 Rev. 1 — Publication officielle](https://csrc.nist.gov/pubs/sp/800/161/r1/final)

### 7.3. Synthèse

Ces références apportent des éclairages complémentaires :

- **ISO/IEC 27036** fournit un cadre pour la sécurité des relations avec les fournisseurs.
- **IEC 62443** permet de replacer ces enjeux dans le contexte des systèmes industriels.
- **Les publications de l'ANSSI et du NIST** contribuent à structurer la gestion des risques liés aux tiers.

La démarche présentée dans cet article vise à traduire ces principes en dispositions opérationnelles adaptées aux contraintes de l'industrie : disponibilité des installations, durée de vie des équipements, maîtrise des configurations, accès aux compétences et capacité réelle à remplacer une solution ou à reprendre une activité.

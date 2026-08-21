---
layout: default
title: "OT : comprendre les technologies opérationnelles"
description: "Comprendre ce que recouvre l'OT, ses différences avec l'IT et les problématiques communes aux environnements industriels, médicaux et autres systèmes cyber-physiques."
category: "comprendre"
tags:
  - OT
  - IT
  - ICS
  - IACS
  - systèmes cyber-physiques
  - cybersécurité industrielle
  - biomédical
date: 2026-08-11
revision: 2026-08-21
chapter: "Fondamentaux"
order: 10
---
<!--
21/08/2026 : remise en page


-->
# OT : comprendre les technologies opérationnelles

**OT** signifie *Operational Technology*, généralement traduit en français par **technologies opérationnelles**.
Le terme désigne l'ensemble des systèmes et technologies utilisés pour **surveiller, contrôler ou agir sur des équipements, des procédés ou des environnements physiques**. 
Dans l'industrie, l'OT permet par exemple de piloter une chaîne de production, contrôler une température, commander une vanne, surveiller une turbine ou assurer le fonctionnement d'un procédé industriel.
Mais l'OT ne se limite pas à l'industrie. Des problématiques comparables peuvent également apparaître dans le domaine de la santé, du transport, de l'énergie, de l'eau, des bâtiments ou d'autres environnements dans lesquels un système numérique interagit directement avec le monde physique.

> **À retenir : l'OT ne traite pas seulement de données. Il participe au fonctionnement d'un environnement physique.**

---

## OT et IT : quelle différence ?

L'**IT** (*Information Technology*) regroupe principalement les technologies utilisées pour traiter, stocker, transmettre et exploiter l'information.

On y retrouve notamment :

- les postes de travail
- les serveurs
- les applications
- les bases de données
- les systèmes de messagerie
- les réseaux informatiques
- les services numériques

L'**OT**, quant à elle, est directement liée à l'observation, au contrôle ou au fonctionnement d'un environnement physique.

On peut schématiquement représenter la différence ainsi :
**IT : l'information**
**OT : l'information au service d'une action ou d'un processus physique**

Cette distinction n'est cependant pas absolue. Les environnements modernes font communiquer de plus en plus les systèmes IT et OT. La frontière entre les deux mondes est donc devenue plus poreuse, alors que leurs contraintes restent souvent différentes.

---

## Un exemple simple

Prenons une installation industrielle qui chauffe un liquide à une température précise.
Dans l'environnement OT :
- un capteur mesure la température
- un automate reçoit cette information
- un programme détermine l'action à effectuer
- une commande agit sur une vanne ou un dispositif de chauffage
- un système de supervision permet à un opérateur de suivre le procédé

L'OT constitue ainsi une chaîne permettant de passer : **du monde physique → à la mesure → à la décision → à l'action.**

Une défaillance ou une attaque informatique peut alors avoir des conséquences qui dépassent largement la perte ou la divulgation de données.

---

## Que trouve-t-on dans un environnement OT ?

Le terme OT recouvre de nombreuses technologies. Dans l'industrie, on retrouve notamment :
- **API** : automates programmables industriels
- **SCADA** : systèmes de supervision et de contrôle
- **DCS** : systèmes de contrôle-commande distribués
- **IHM** : interfaces homme-machine (ecran tactile pour de la commande locale)
- **capteurs et actionneurs**
- **équipements de contrôle-commande**
- **réseaux industriels**
- **systèmes instrumentés de sécurité**
- **postes d'ingénierie et de maintenance**

L'ensemble de ces composants peut constituer un ICS (*Industrial Control System*) ou, selon le contexte, un IACS (*Industrial Automation and Control System*). Ces termes ne sont pas strictement interchangeables. OT est un terme large. ICS et IACS désignent plus spécifiquement des ensembles de systèmes de contrôle et d'automatisation industriels.

---

## OT ne signifie pas uniquement « industrie »

Le terme OT est souvent associé à l'industrie, mais certaines problématiques rencontrées dans les environnements industriels existent également dans d'autres secteurs. On peut notamment rencontrer des systèmes cyber-physiques dans :
- l'énergie
- les transports
- l'eau et l'assainissement
- les bâtiments
- les infrastructures
- la santé
- les laboratoires
- certains environnements scientifiques

L'objectif n'est pas de considérer que tous ces environnements sont identiques.

Ils possèdent leurs propres architectures, réglementations, métiers, contraintes et référentiels.

En revanche, certaines questions de cybersécurité sont communes :

> **Que se passe-t-il si le système s'arrête ?**

> **Que se passe-t-il si son fonctionnement est modifié ?**

> **Peut-on appliquer un correctif sans interrompre le service ?**

> **Qui peut intervenir sur l'équipement ?**

> **Qui valide une modification ?**

Ces questions constituent un terrain commun entre différents domaines.

---

## OT et biomédical : des problématiques qui se croisent

Le domaine médical constitue un exemple particulièrement intéressant. Un dispositif médical ou un équipement biomédical n'est pas nécessairement considéré comme de l'OT au sens strict.
Il peut cependant présenter plusieurs caractéristiques comparables à celles rencontrées dans les environnements industriels :

- interaction avec le monde physique
- exigences fortes de disponibilité
- importance de l'intégrité des mesures et des commandes
- dépendance au constructeur
- logiciels propriétaires
- longue durée de vie
- contraintes de maintenance
- mises à jour difficiles à réaliser
- accès de maintenance
- environnement technique hétérogène
- conséquences physiques possibles d'une défaillance.

La comparaison ne signifie pas qu'un équipement biomédical et un système industriel sont équivalents. Elle permet plutôt d'identifier des **problématiques cyber-physiques communes**.

### Un exemple parlant

On entend parfois :

> « Dans le médical, on ne peut pas arrêter un respirateur comme ça. »
La même logique existe dans de nombreux environnements industriels : **On ne peut pas non plus arrêter n'importe comment un système de refroidissement, un procédé chimique, une installation électrique ou un système de contrôle-commande critique.** Les conséquences et les mécanismes de sûreté ne sont évidemment pas les mêmes.

Mais la question de fond peut être commune :
**Quelles sont les conséquences d'une indisponibilité ou d'une modification non maîtrisée d'un système numérique qui participe au fonctionnement d'un environnement physique ?** Cette approche permet de faire circuler les bonnes pratiques entre secteurs plutôt que de cloisonner artificiellement les connaissances.

---

## Des contraintes différentes, mais des questions parfois communes

Un hôpital, une centrale de production d'énergie, une usine et un réseau d'eau ne fonctionnent évidemment pas de la même manière. Pour autant, leurs équipes peuvent être confrontées à des questions similaires :

| Question | Problématique |
|---|---|
| Peut-on arrêter le système ? | Disponibilité |
| Peut-on redémarrer le système ? | Continuité de service |
| Peut-on appliquer un correctif ? | Maintenance et gestion du changement |
| Qui autorise l'intervention ? | Gouvernance |
| Qui maîtrise la configuration ? | Intégrité |
| Qui peut accéder au système ? | Contrôle des accès |
| Que se passe-t-il en cas de compromission ? | Gestion des incidents |
| Que se passe-t-il si le fournisseur disparaît ? | Cycle de vie et dépendance fournisseur |
| Quelle est la conséquence d'une commande erronée ? | Impact physique / sûreté |

C'est cette proximité des problématiques qui rend intéressantes les comparaisons entre secteurs.

---

## Pourquoi l'OT est-il particulier ?

### Disponibilité
L'arrêt d'un système OT peut provoquer l'arrêt d'une production, l'indisponibilité d'un service ou la dégradation d'un procédé. Une opération de cybersécurité qui serait anodine en IT peut donc être risquée en OT.

### Intégrité
Une information erronée peut conduire un système à prendre une mauvaise décision ou à commander incorrectement un équipement. L'intégrité des mesures, des programmes et des commandes est donc essentielle.

### Sûreté
Dans certains environnements, un dysfonctionnement peut avoir des conséquences sur la sécurité des personnes ou sur l'environnement. La cybersécurité peut alors contribuer à la **sûreté de fonctionnement**, sans pour autant se confondre avec elle.

### Durée de vie

Les équipements opérationnels peuvent rester en service pendant plusieurs décennies. Il n'est donc pas rare de rencontrer des systèmes anciens, des logiciels qui ne sont plus supportés ou des équipements difficiles à remplacer.

### Maintenance
Les opérations de maintenance peuvent être réalisées dans des conditions particulières et avec des fenêtres d'intervention limitées.

### Fournisseurs
Un système opérationnel fait fréquemment intervenir de nombreux acteurs :

- fabricant
- intégrateur
- automaticien
- mainteneur
- exploitant
- fournisseur de logiciel
- sous-traitants

La cybersécurité doit donc également prendre en compte la chaîne d'approvisionnement.

---

## OT et cybersécurité

La cybersécurité OT vise à protéger les systèmes opérationnels contre les événements susceptibles de compromettre leur fonctionnement, leur intégrité ou leur sécurité. Les conséquences potentielles d'une compromission peuvent être très différentes de celles observées dans un environnement bureautique.

Une attaque peut par exemple chercher à :
- arrêter une installation
- modifier un paramètre de procédé
- empêcher un opérateur de surveiller l'installation
- modifier un programme automate
- perturber les communications industrielles
- compromettre un poste d'ingénierie
- utiliser un fournisseur ou un accès de maintenance comme point d'entrée.

La cybersécurité OT doit donc tenir compte **du procédé et de ses conséquences**, et pas uniquement de la technologie informatique.

---

## OT ne signifie pas « réseau industriel »
Il est tentant de réduire l'OT aux équipements et aux réseaux industriels. Cette vision est trop restrictive.

L'environnement OT comprend également :
- les personnes
- les procédures
- les postes d'ingénierie
- les outils de maintenance
- les systèmes de supervision
- les fournisseurs
- les accès distants
- les logiciels
- les configurations
- les données nécessaires au fonctionnement du procédé
La sécurité d'un système OT doit donc être considérée comme un ensemble.

---

## Une différence fondamentale avec l'IT

Dans un environnement informatique classique, on peut souvent remplacer rapidement un équipement, réinstaller un système ou appliquer une mise à jour.
Dans un environnement opérationnel, ce n'est pas toujours possible.

Avant de modifier un système OT, il faut notamment se demander :
- Quel est l'impact sur le procédé ou le service ?
- Peut-on arrêter l'installation ?
- Le système est-il supporté par son constructeur ?
- La modification a-t-elle été testée ?
- Existe-t-il une procédure de retour arrière ?
- Quelles sont les conséquences d'une indisponibilité ?
- Qui est responsable de la validation de la modification ?

C'est pourquoi une bonne pratique de sécurité informatique ne peut pas toujours être transposée directement à l'OT.

> **Sécuriser l'OT, c'est sécuriser un système numérique qui participe au fonctionnement d'un système physique, en tenant compte de son contexte > et de ses conséquences.**

---

## OT et cycle de vie

La cybersécurité OT doit être prise en compte tout au long du cycle de vie d'un système opérationnel :
**conception → études → réalisation → intégration → mise en service → exploitation → maintenance → évolution → retrait**

---

## OT et systèmes critiques

La notion d'OT devient particulièrement intéressante lorsqu'un système numérique participe au fonctionnement d'une infrastructure ou d'un service critique. La criticité ne dépend pas uniquement de la technologie utilisée.

Elle dépend notamment :
- de la fonction assurée
- des conséquences d'une indisponibilité
- des conséquences d'une perte d'intégrité
- des dépendances à d'autres systèmes
- des possibilités de fonctionnement dégradé
- des moyens de secours
- du temps disponible pour réagir

Ainsi, deux systèmes utilisant une technologie similaire peuvent avoir des niveaux de criticité très différents. Inversement, des systèmes appartenant à des secteurs différents peuvent présenter des contraintes de cybersécurité comparables.

---

## Une approche transversale

CyberRepères utilise ici le terme **OT** comme une porte d'entrée vers les problématiques de cybersécurité des systèmes opérationnels et cyber-physiques. Cette approche ne cherche pas à effacer les différences entre les secteurs. Elle vise au contraire à identifier ce qui peut être partagé :

- méthodes
- bonnes pratiques
- principes d'architecture
- gestion des accès
- gestion des changements
- maintenance
- gestion des fournisseurs
- gestion des incidents
- continuité d'activité
- protection des configurations
- retour d'expérience

Les référentiels restent ensuite à étudier dans leur propre contexte.

---

## Notions associées

Cette fiche introduit plusieurs notions qui pourront être approfondies séparément :

- [MOA et MOE](moa-moe.md) ;
- ICS
- IACS
- SCADA
- API
- IHM / HMI
- systèmes cyber-physiques
- segmentation réseau
- défense en profondeur
- Zero Trust
- cybersécurité industrielle
- cybersécurité des dispositifs médicaux

---

## Référentiels associés

Plusieurs organismes publient des normes, référentiels et guides permettant d'approfondir les problématiques liées aux systèmes opérationnels.

Parmi eux :

- **IEC**, notamment avec la série IEC 62443
- **ANSSI**, avec ses publications relatives aux systèmes industriels
- **CLUSIF**, avec ses travaux consacrés à la cybersécurité industrielle
- **SANS Institute**, notamment au travers de sa littérature consacrée à l'OT
- **NIST**, avec différentes publications relatives aux systèmes de contrôle industriels et aux systèmes cyber-physiques
- d'autres organismes spécialisés selon les secteurs concernés

Les documents n'ont pas tous le même statut ni le même objectif. Il est donc important de distinguer les normes, réglementations, guides, méthodes et publications de retour d'expérience.

---

## À retenir

> **L'OT désigne les technologies qui permettent de surveiller, contrôler ou agir sur des équipements, des procédés ou des environnements physiques.**

L'OT est souvent associée à l'industrie, mais certaines problématiques peuvent également être rencontrées dans d'autres secteurs, notamment la santé, l'énergie, les transports, l'eau ou les bâtiments.
Les environnements sont différents, mais les questions fondamentales peuvent parfois être proches :
**Peut-on arrêter ? Peut-on modifier ? Peut-on mettre à jour ? Qui peut intervenir ? Et quelles sont les conséquences si le système ne fonctionne plus comme prévu ?**
La cybersécurité OT doit donc prendre en compte **la technologie, le procédé, les personnes, le cycle de vie, les fournisseurs et surtout les conséquences possibles d'un dysfonctionnement ou d'une compromission.**


---
layout: default
title: "BIA, analyse de risque, AMDEC : arrêtons de les confondre"
description: "Trois méthodes, trois questions différentes. Comment distinguer le BIA, l'analyse de risque et l'AMDEC, et pourquoi elles sont complémentaires."
category: "comprendre"
tags: 
  - continuité d'activité
  - gestion des risques 
  - BIA 
  - AMDEC 
  - Sûreté de fonctionnement
date: 2026-11-17
revision: 2026-10-25
chapter: "Fondamentaux"
order: 10
comments: true
---

---

# BIA, analyse de risque, AMDEC : arrêtons de les confondre

Autour de moi, trop de gens mélangent ces trois démarches. On entend « on a fait un BIA, donc on a analysé nos risques » ou « notre AMDEC, c'est notre analyse de risque ». Non. Ces trois méthodes ne répondent **pas à la même question**, ne partent **pas du même endroit** et ne s'adressent **pas aux mêmes personnes**.

Voici comment les distinguer en quelques minutes.

## Le BIA : le domaine du « et alors ? »

Le **BIA** (*Business Impact Analysis*, ou bilan d'impact sur l'activité) ne se demande **pas** si l'événement peut arriver. Il part du principe que la perte a eu lieu et mesure les conséquences.

On ne pose donc pas la question « le datacenter peut-il être inondé ? ». On pose la question : **« si le datacenter n'est plus disponible, et alors ? »**

Peu importe la cause : inondation, incendie, cyberattaque, panne électrique. Ce qui compte, c'est l'impact sur les activités de l'organisation au fil du temps. Le BIA produit notamment :

- la **DMIA / MTPD** : la durée maximale d'interruption admissible avant que les conséquences deviennent inacceptables ;
- le **RTO** : le délai de reprise visé ;
- le **RPO** : la quantité de données que l'on accepte de perdre.

Il s'adresse aux **métiers et à la direction**, car ce sont eux qui savent ce qui est vital pour l'activité.

## L'analyse de risque : « que peut-il arriver, et à quel point ? »

L'**analyse de risque** (AR) travaille sur des **scénarios** : une menace exploite une vulnérabilité et provoque un dommage. Pour chaque scénario, on estime :

- la **gravité** (l'impact) ;
- la **vraisemblance** (la probabilité que cela arrive).

Le plus souvent, on obtient un score, **Gravité × Vraisemblance**, qui permet de **prioriser** les risques et de décider quoi traiter en premier.

### On ne peut pas toujours agir sur la vraisemblance

Pour une menace externe (inondation, cyberattaque), on ne maîtrise pas toujours la probabilité d'occurrence. Mais l'analyse de risque ne se limite pas à la prévention. Un risque se traite de plusieurs façons :

| Levier | Effet | Exemples |
|---|---|---|
| **Prévention** | Réduit la vraisemblance | Durcissement, contrôle d'accès, maintenance |
| **Protection** | Réduit la gravité | Sauvegardes, redondance, plan de continuité |
| **Transfert** | Réduit l'impact financier | Assurance, sous-traitance |
| **Acceptation** | Aucun, mais en connaissance de cause | Risque faible ou coût de traitement disproportionné |

C'est ici que le BIA et l'AR se rejoignent : **le BIA alimente l'estimation de la gravité** dans l'analyse de risque.

## L'AMDEC : « comment ça peut défaillir, et le verra-t-on ? »

L'**AMDEC** (Analyse des Modes de Défaillance, de leurs Effets et de leur Criticité, *FMEA* en anglais) est une approche **bottom-up**. On part d'un système, on le décompose en composants et en fonctions, puis pour chacun on cherche :

- les **modes de défaillance** (comment ça peut tomber en panne) ;
- leurs **causes** et leurs **effets** ;
- leur **criticité**, cotée selon trois axes : **Gravité × Occurrence × Détection**.

La **détection** est ce qui la distingue de l'analyse de risque classique à deux axes : une défaillance grave mais détectée à temps n'a pas le même poids qu'une défaillance silencieuse.

Née dans l'aéronautique et l'automobile, l'AMDEC parle aux **concepteurs, mécaniciens, électroniciens, ingénieurs process**. Elle débouche sur des actions correctives, souvent directement sur la conception.

## Le tableau comparatif

| | **BIA** | **Analyse de risque** | **AMDEC** |
|---|---|---|---|
| **Question** | Et alors ? | Que peut-il arriver, et à quel point est-ce grave et probable ? | Comment ça peut défaillir, et comment le détecter ? |
| **Point de départ** | Les activités et processus | Les menaces et vulnérabilités | Les composants et fonctions |
| **Approche** | Impact, indépendant de la cause | Scénarios | Bottom-up, par mode de défaillance |
| **Cotation** | Durées et seuils (DMIA, RTO, RPO) | Gravité × Vraisemblance | Gravité × Occurrence × Détection |
| **Sortie** | Criticité des activités, objectifs de reprise | Priorisation et plan de traitement | Actions correctives sur la conception |
| **Public** | Métiers, direction | RSSI, risk managers | Ingénieurs, concepteurs |

## Un même exemple, trois regards : le datacenter

- **BIA** : « Sans le datacenter, la facturation s'arrête après 4 heures et les pertes deviennent critiques au-delà d'une journée. »
- **Analyse de risque** : « Le scénario d'inondation est plausible sur ce site. Voici la priorité du risque et les mesures à engager (surélévation, site de secours, assurance). »
- **AMDEC** : « La pompe de relevage peut tomber en panne selon tel mode, sans alarme, avec tel effet sur la salle serveurs. Il faut ajouter une redondance et une détection. »

## En résumé : des méthodes complémentaires

Le BIA, l'analyse de risque et l'AMDEC ne sont **pas concurrentes**. Elles s'enchaînent :

1. Le **BIA** identifie ce qui est vital et à quelle vitesse.
2. L'**analyse de risque** détermine ce qui menace ces activités et comment les traiter.
3. L'**AMDEC** descend au niveau technique pour fiabiliser les systèmes qui les supportent.

Les confondre, c'est se retrouver avec un angle mort : un BIA sans analyse de risque ne dit pas quoi faire ; une analyse de risque sans BIA estime mal la gravité ; une AMDEC sans les deux optimise parfois ce qui n'est pas critique.

[ Télécharger la présentation sur le sujet – format PowerPoint ]({{ '/comprendre/sources/BIA_AnalyseRisque_AMDEC_CyberReperes.pptx' | relative_url }})

## Un cas concret : la cyberattaque des systèmes frigorifiques d'octobre 2026

### 1. Quand une installation frigorifique devient une cible cyber

Dans la nuit du 11 au 12 octobre 2026, plusieurs centaines de supermarchés français sont victimes d'une cyberattaque ciblant leurs installations frigorifiques.

Les attaquants prennent le contrôle à distance de contrôleurs chargés de piloter les équipements de réfrigération. Parmi les matériels concernés figurent notamment des contrôleurs Danfoss, ainsi que des équipements d'autres constructeurs.

Les paramètres de régulation et les cycles de dégivrage sont modifiés, provoquant une élévation anormale de la température des chambres froides et des meubles réfrigérés. Les conséquences sont particulièrement concrètes : destruction de marchandises, pertes financières et départs de feu dans certains magasins.

L'incident met notamment en évidence la vulnérabilité d'équipements parfois anciens, en fin de support, et dont les interfaces de télégestion étaient insuffisamment protégées.

Cet événement illustre une réalité parfois sous-estimée : un équipement dont la fonction première est de maintenir des denrées au froid peut devenir un point de défaillance majeur pour toute une activité.

### 2. Trois démarches, trois occasions d'identifier le problème

Avec le recul, cet événement soulève une question : comment une telle dépendance a-t-elle pu passer inaperçue ?

Le problème aurait pourtant pu être identifié à différents niveaux, par des acteurs différents et au travers de trois démarches complémentaires.

**L'exploitant : le BIA aurait révélé l'impact métier**

L'exploitant du magasin ou de l'enseigne aurait pu commander un BIA (*Business Impact Analysis*) afin d'identifier les conséquences d'une indisponibilité de ses installations frigorifiques.

Que se passe-t-il si les chambres froides ne maintiennent plus les températures requises pendant plusieurs heures ? Quelles marchandises sont perdues ? Combien de temps l'activité peut-elle fonctionner sans réfrigération ? Quelles sont les conséquences financières, commerciales et éventuellement sanitaires ?

Le BIA aurait permis de mettre en évidence la criticité de cette fonction pour l'activité, indépendamment de la cause de son indisponibilité.

**Les équipes cybersécurité : l'analyse de risque aurait identifié le scénario**

Les équipes cybersécurité auraient pu conduire une analyse de risque sur les systèmes de télégestion et de régulation frigorifique.

Un contrôleur accessible à distance, potentiellement obsolète, dont la compromission permet de modifier les paramètres de fonctionnement d'une installation : le scénario mérite clairement d'être étudié.

Une analyse de risque aurait permis d'identifier les menaces, les vulnérabilités et les conséquences d'une compromission, puis de définir les mesures de traitement adaptées : sécurisation des accès distants, cloisonnement réseau, maintien en condition de sécurité et surveillance.

**Le frigoriste : l'AMDEC aurait révélé les dépendances techniques**

Enfin, le frigoriste, en tant que concepteur ou intégrateur de l'installation, aurait pu réaliser une AMDEC (*Analyse des Modes de Défaillance, de leurs Effets et de leur Criticité*).

L'analyse des fonctions de régulation aurait notamment pu mettre en évidence un point unique de défaillance (*Single Point Of Failure – SPOF*) : un contrôleur unique capable de compromettre la maîtrise de l'ensemble de l'installation.

Elle aurait également pu identifier l'absence de surveillance indépendante, la dépendance aux interfaces de télégestion ou encore l'absence de fonctionnement en mode dégradé.

Ces constats auraient pu conduire à revoir l'architecture technique et à prévoir des dispositifs permettant de limiter les conséquences d'une défaillance ou d'une compromission.

**Trois démarches, trois angles d'analyse, une même problématique.**

| Démarche | Acteur concerné | Ce qu'elle aurait pu révéler |
|---|---|---|
| BIA | Exploitant / métiers | La criticité de la fonction frigorifique et les conséquences de son indisponibilité |
| Analyse de risque | Équipes cybersécurité | Le scénario de compromission des systèmes de régulation et ses conséquences |
| AMDEC | Frigoriste / concepteur | Les points uniques de défaillance et les faiblesses de conception |

Ces trois démarches ne garantissent évidemment pas qu'une attaque aurait été empêchée. Elles auraient néanmoins offert trois occasions distinctes d'identifier la criticité du système, ses vulnérabilités et ses dépendances.

**La cybersécurité ne peut pas reposer uniquement sur les équipes cyber.** L'exploitant doit connaître les conséquences d'une interruption, le concepteur doit fiabiliser son installation et les équipes cybersécurité doivent identifier les scénarios de compromission.

C'est précisément pour cela que le BIA, l'analyse de risque et l'AMDEC sont complémentaires : chacun apporte un éclairage différent sur une même réalité.

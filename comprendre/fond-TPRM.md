---
layout: default
title: "TPRM - Gestion des tiers : maîtriser les risques liés à ses fournisseurs"
description: "On explique ce que c'est la gestion des tiers, et comment s'y prendre ? Les étaptes etc"
category: "comprendre"
tags:
  - TPRM
  - Plan de sortie
  - ICS
  - dépendances
  - Gestions des tiers
  - cybersécurité industrielle
  - Gouvernance
date: 2026-10-14
revision: 2026-10-14
chapter: "Fondamentaux"
order: 40
comments: true
---

# Gestion des tiers : maîtriser les risques liés à ses fournisseurs

## Qu'entend-on par tiers ?

Un tiers, c'est toute organisation extérieure à la vôtre qui contribue à son fonctionnement : fournisseurs, prestataires, sous-traitants, intégrateurs, partenaires ou encore éditeurs de logiciels.

Le prestataire de votre prestataire, c'est aussi potentiellement votre problème. Et bien souvent, vous ignorez jusqu'à son existence. Vous pensez peut-être que tout cela reste un peu théorique. Pourtant, les conséquences peuvent être très concrètes.

## Quand la chaîne du froid devient une cible

Dans la nuit du 11 au 12 octobre 2026, des systèmes de régulation frigorifique de plusieurs centaines de supermarchés français — près de 500 selon les enseignes concernées — ont été compromis. Les attaquants ont déclenché à distance des cycles de dégivrage forcé et relevé les consignes de température jusqu'à 50 °C. Au matin, vitrines réfrigérées, chambres froides et congélateurs ne refroidissaient plus : rupture de la chaîne du froid, produits frais et surgelés à jeter, et, selon le parquet de Paris, qui a ouvert une enquête, des départs de feu. Les pertes peuvent atteindre 200 000 € pour un seul hypermarché.

Les équipements concernés comprenaient notamment des contrôleurs du fabricant danois Danfoss (séries AK-SM et AK-SC), mais aussi des systèmes d'autres fabricants, dont Copeland et Dixell. Dans son alerte du 12 octobre, mise à jour le lendemain, le CERT-FR a signalé de « nombreuses compromissions » et rappelé les risques liés à l'exposition des interfaces d'administration sur Internet. L'ANSSI a jugé urgent de déconnecter ces contrôleurs d'Internet ou, à défaut, d'adopter une politique de filtrage réseau très restrictive.

- [CERT-FR Incident de sécurité ciblant les contrôleurs à distance des installations de réfrigération](https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/)

Détail important : selon le fabricant, la majorité des unités touchées étaient des produits anciens, arrivés en fin de vie, qui ne bénéficiaient plus de mises à jour logicielles ni de correctifs de sécurité.

L'origine exacte de chaque compromission reste à établir. Rien ne permet d'affirmer que les attaquants sont passés par un prestataire de maintenance ou qu'ils ont compromis les systèmes internes d'un fabricant.

Mais cet incident fait surtout apparaître une chaîne de dépendances. Les enseignes touchées ne sont pas clientes directes du fabricant : elles dépendent de frigoristes et d'acteurs de maintenance qui installent et maintiennent ces équipements. Or des vulnérabilités affectant ces contrôleurs avaient été documentées plusieurs semaines avant l'attaque. Les alertes ont-elles été relayées jusqu'aux exploitants ? Ont-elles débouché sur les migrations nécessaires ? L'enquête devra le dire.

Même si vraisemblablement personne n'a consommé de nourriture avarié, cette affaire soulève en tout cas une question essentielle : qui est responsable de la sécurité de ces équipements, de leurs mises à jour, de leur configuration et des accès distants qui permettent de les maintenir ?

Le fabricant fournit le matériel. L'intégrateur ou le frigoriste l'installe et le maintient. L'exploitant dépend de son bon fonctionnement. Et lorsque quelque chose tourne mal, les conséquences sont bien réelles.

C'est précisément l'un des enjeux de la gestion des risques liés aux tiers : connaître ses dépendances, définir clairement les responsabilités et vérifier que les risques sont maîtrisés tout au long de la relation.

## Une démarche qui suit le cycle de vie du fournisseur

La bonne nouvelle, c'est qu'il existe une démarche structurée. Elle suit le cycle de vie de la relation avec le fournisseur, depuis le moment où vous envisagez de travailler avec lui jusqu'au jour où vous vous en séparez. C'est ce que l'on appelle la gestion des tiers ou TPRM (pour Third Party Risk Management en anglais).

### 1. Cartographier et évaluer les tiers

La première étape consiste à savoir qui sont vos tiers. Cela paraît évident et pourtant, beaucoup d'organisations seraient bien incapables d'en dresser la liste complète.

Une fois les tiers identifiés, il faut les classer, car tous les fournisseurs ne présentent pas le même niveau de risque.

Le distributeur de pièces d'automatisme et l'intégrateur qui dispose d'un accès distant à votre réseau industriel ne représentent évidemment pas le même risque. Mais attention : un fournisseur peut aussi être critique sans disposer du moindre accès informatique, simplement parce que votre activité dépend de ses produits ou de ses compétences.

Pour évaluer la criticité d'un tiers, quelques questions simples permettent de commencer :

- A-t-il accès à nos systèmes ? À quels équipements et avec quels privilèges ?
- A-t-il accès à des données ? Si oui, lesquelles ?
- Peut-il modifier des configurations, des programmes d'automates ou des paramètres de fonctionnement ?
- S'il disparaît demain, notre activité s'arrête-t-elle ? Pourrions-nous facilement le remplacer ?
- Une compromission de ses systèmes pourrait-elle affecter notre production ou la sécurité des personnes ?

Pour les tiers les plus critiques, on procède ensuite à ce qu'on appelle une *due diligence*, c'est-à-dire une vérification approfondie avant de s'engager.

On examine notamment sa situation financière, son niveau de sécurité, ses certifications, ses propres dépendances et les incidents qu'il a pu connaître. On cherche aussi à comprendre comment il gère les accès, les vulnérabilités, les mises à jour et ses propres sous-traitants.

Le mot important ici, c'est **proportionnalité**.

On ne fait pas passer au distributeur de pièces d'automatisme le même examen qu'à l'intégrateur qui dispose d'un accès au réseau industriel. Sinon, vous allez noyer vos équipes sous la paperasse et, au final, plus personne ne regardera rien sérieusement.

L'objectif n'est pas de tout vérifier chez tout le monde, mais de concentrer les efforts là où les conséquences potentielles sont les plus importantes.

### 2. Contractualiser les exigences de sécurité

Le contrat est un levier essentiel de maîtrise du risque. Pourtant, très souvent, on le laisse entièrement aux juristes et aux acheteurs sans associer suffisamment les équipes de sécurité.

Or, c'est dans le contrat que vous fixez les exigences que le fournisseur devra respecter, pour cela il y notamment le PAS (plan d'assurance sécurité).

Quelles mesures de sécurité doit-il appliquer ? Dans quel délai doit-il vous prévenir s'il subit un incident susceptible de vous affecter ? Où vos données seront-elles stockées ? A-t-il le droit de sous-traiter une partie du travail ? Et à quelles conditions ? Pouvez-vous vérifier le respect de ses engagements ? Que se passera-t-il si vous décidez de vous séparer ?

En environnement industriel, il faut aussi préciser les responsabilités relatives à la maintenance, aux correctifs de sécurité, à la gestion des accès distants, à la sauvegarde des configurations de vos automates et à la disponibilité des équipements.

Et surtout, gardez ceci en tête : **une fois le contrat signé, votre pouvoir de négociation peut fondre comme neige au soleil.**

C'est avant qu'il faut obtenir les garanties nécessaires.

Bien entendu, toutes les exigences ne sont pas toujours négociables, notamment face à un grand fournisseur. Mais lorsqu'une clause est impossible à obtenir, il reste nécessaire d'évaluer le risque résiduel et de rechercher, si possible, des mesures compensatoires.

Et rappelez-vous enfin : **on délègue des tâches, on ne délègue jamais la responsabilité.** Devant le régulateur, le juge ou vos clients, c'est toujours vous qui répondez, même quand le travail a été externalisé. Deux affaires, racontées en annexe de cet article, l'illustrent.

### 3. Surveiller les tiers dans la durée

C'est souvent là que le bât blesse : beaucoup d'organisations évaluent leurs fournisseurs une fois, au moment de la signature, puis ne regardent plus jamais ce qui se passe. Or, un fournisseur évolue, tout comme ses produits, ses pratiques et ses propres dépendances.

La gestion du risque ne s'arrête donc pas à la signature du contrat. Elle nécessite une surveillance continue, avec des revues régulières et proportionnées à la criticité du tiers.

Un questionnaire vous indique ce que votre fournisseur déclare faire. Il ne vous garantit pas, à lui seul, ce qu'il fait réellement.

C'est pourquoi, pour les tiers les plus critiques, il faut pouvoir confronter les déclarations à des éléments concrets : rapports d'audit, preuves de mise en œuvre, état des accès, gestion des vulnérabilités ou respect des engagements contractuels.

Il ne s'agit pas de considérer chaque fournisseur comme suspect, mais de vérifier que les mesures attendues sont effectivement en place et qu'elles restent adaptées.

Il faut également surveiller les changements susceptibles de modifier le risque : un rachat, un changement de sous-traitant, une évolution des accès, une vulnérabilité majeure ou la fin du support d'un équipement. L'attaque d'octobre 2026 l'a brutalement rappelé : plusieurs contrôleurs compromis étaient en fin de vie depuis des années, sans correctifs disponibles.

Un fournisseur jugé peu critique il y a deux ans peut ne plus l'être aujourd'hui.

### 4. Préparer la sortie dès le début

Au moment de signer le contrat, on est dans l'enthousiasme du début de la relation. Personne n'aime parler de divorce le jour du mariage.

Et pourtant, il faut se poser la question : si demain je dois quitter ce fournisseur, parce qu'il fait faillite, parce qu'il ne répond plus à mes besoins ou parce qu'il a été racheté par un concurrent, comment est-ce que je fais ?

Puis-je récupérer mes données dans un format exploitable ? Ai-je accès aux configurations, à la documentation et aux compétences nécessaires ? Combien de temps me faudrait-il pour basculer vers un autre système ? Existe-t-il seulement une autre solution ?

C'est ce qu'on appelle la stratégie de sortie, ou la réversibilité, un sujet qui fait l'objet d'une page dédiée sur CyberRepères.

Cette réflexion doit commencer avant la signature, se traduire dans le contrat et être réévaluée pendant toute la relation.

En environnement industriel, récupérer des fichiers ne suffit pas toujours. Encore faut-il disposer des logiciels compatibles, des licences, des pièces détachées et des compétences nécessaires pour remettre le système en service. Et tout cela doit pouvoir être organisé sans mettre en péril la continuité de l'exploitation.

### Une exigence de plus en plus importante

La directive européenne NIS2 renforce l'importance de la sécurité de la chaîne d'approvisionnement pour les entités qui entrent dans son champ d'application. Elle prévoit notamment de prendre en compte les risques liés aux relations avec les fournisseurs et les prestataires de services.

Le mouvement est général : les organisations doivent mieux connaître leurs dépendances et ne plus considérer la sécurité de leurs fournisseurs comme un sujet extérieur à leur propre responsabilité.

## Pas seulement l'affaire de l'exploitant

À lire ce qui précède, on pourrait croire que la gestion des tiers est l'affaire de l'exploitant, celui qui fait tourner l'installation au quotidien. C'est plus subtil que cela : c'est l'affaire de tous, y compris — et peut-être d'abord — de ceux qui conçoivent et construisent.

La plupart des dépendances dont l'exploitant hérite ont été créées en amont, au moment d'un projet. C'est en phase de conception, lors d'un chantier neuf ou d'une extension, que l'on choisit un équipement, un intégrateur, une solution d'accès distant, un éditeur de logiciel. Ces choix, souvent arbitrés sur le coût d'investissement (CAPEX), engagent l'exploitation pour des années, voire des décennies en environnement industriel. Et leurs conséquences se paient en exploitation (OPEX) : maintenance, correctifs, remplacement, réversibilité.

Il ne s'agit surtout pas d'opposer projet et exploitation. L'information est dans le projet ; le risque est dans l'exploitation. Chacun a sa part.

On entend pourtant souvent, en fin de projet : « c'est l'exploitant qui gérera ça plus tard. » Plus tard, c'est-à-dire quand l'équipe projet se sera dispersée, que la documentation se sera perdue, que les comptes de maintenance auront changé plusieurs fois de mains et que personne ne se souviendra plus qui accède à quoi, ni pourquoi. Reconstruire la cartographie des dépendances des années après la mise en service coûte infiniment plus cher que la documenter pendant le projet.

Car c'est bien le paradoxe : dresser la liste des dépendances n'a jamais été aussi facile qu'en phase de projet. On sait quels équipements on installe, qui les fournit, qui les met en service, qui y accède à distance, avec quels comptes et quels outils. Il ne reste qu'à l'écrire.

Concrètement, ce que le projet devrait remettre à l'exploitant avec l'installation :

- la cartographie des dépendances créées : fournisseurs, intégrateurs, sous-traitants et, autant que possible, leurs propres sous-traitants ;
- la liste des accès distants et des comptes de maintenance, avec leurs privilèges ;
- l'état des configurations et leurs sauvegardes : programmes d'automates, paramétrages des contrôleurs, réglages des équipements ;
- les documents de sécurité qui permettront à l'exploitant de démarrer sa démarche : analyse d'impacts (BIA), plan de sortie ou stratégie de réversibilité, contrats de support et leurs durées, et surtout les dates de fin de vie et de fin de support prévisionnelles des équipements.

Rien de tout cela n'est compliqué à produire quand on est en train de faire ces choix : l'information existe déjà dans les dossiers du projet. Il s'agit de l'organiser, de la compléter côté sécurité et de la remettre proprement. Pour une maîtrise d'œuvre, c'est d'ailleurs un livrable à part entière, simple à produire au bon moment et qui prendra de plus en plus de valeur.

L'attaque d'octobre 2026 illustre ce que coûte ce fil coupé entre projet et exploitation : des contrôleurs installés il y a des années, dont certains modèles avaient été déclarés en fin de vie dès 2021, et dont personne n'a planifié la migration. Si, au moment de leur installation, la dépendance et son cycle de vie avaient été documentées et remises à l'exploitant, la migration aurait pu être anticipée — au lieu d'être découverte dans une vitrine à 50 °C.

Maintenant, soyons honnêtes : sur le papier, tout cela est très clair. Mais dans la réalité, la gestion des risques liés aux tiers est un exercice difficile, et il existe quelques pièges classiques.

## Les pièges à éviter

### 1. Le questionnaire qui finit dans un tiroir

Vous envoyez à votre fournisseur un questionnaire de sécurité de plusieurs centaines de questions. Il le remplit en cochant « oui » partout. Vous le rangez dans un dossier, personne ne le relit, personne ne vérifie les réponses.

Vous avez peut-être satisfait une exigence documentaire, mais vous n'avez pas nécessairement une vision fiable du niveau de sécurité de votre fournisseur.

Le questionnaire est un outil, pas une preuve suffisante. Il doit être adapté au risque et, lorsque c'est nécessaire, complété par des vérifications.

### 2. L'évaluation unique, réalisée à la signature

Vous évaluez votre fournisseur une fois, au début de la relation, puis vous n'y revenez jamais.

Or, un fournisseur évolue, ses produits aussi, et votre évaluation vieillit avec lui. Une réévaluation périodique, complétée par une réévaluation après un changement important, permet de conserver une vision plus juste du risque.

### 3. Le fournisseur jugé sans importance

Vous classez un fournisseur en risque faible parce qu'il ne traite pas de données sensibles. Mais vous avez oublié qu'il dispose d'un accès distant à votre réseau industriel.

Rappelez-vous la cartographie : la criticité d'un tiers ne dépend pas seulement de ce qu'il fait pour vous, mais aussi de ce qu'il peut atteindre chez vous. Un prestataire qui ne traite aucune donnée personnelle peut parfaitement représenter un risque important s'il peut intervenir sur un automate ou modifier les paramètres d'un système de contrôle.

### 4. Le rapport de force contractuel

Vous êtes face à un géant. Vous souhaitez imposer vos propres exigences de sécurité, mais votre fournisseur vous présente son contrat standard : c'est à prendre ou à laisser.

Vous ne pourrez peut-être ni l'auditer directement ni obtenir toutes les clauses souhaitées.

Cela ne signifie pas pour autant que vous êtes sans solution. Vous pouvez rechercher des garanties alternatives, limiter les accès, renforcer la surveillance, réduire votre dépendance ou formaliser le risque résiduel pour qu'il soit accepté au bon niveau de responsabilité.

Et si le risque reste incompatible avec vos exigences, il faut pouvoir envisager une autre solution.

## Par où commencer concrètement ?

L'objectif n'est pas d'atteindre le risque zéro. Il n'existe pas. Il s'agit de savoir où se trouvent vos dépendances, de connaître les plus critiques et d'être prêt le jour où l'une d'elles fera défaut.

Vous n'avez pas besoin de lancer un programme complexe pour commencer.

Pour vos tiers les plus critiques :

- **Relisez les contrats.** Prévoient-ils une notification des incidents, des exigences de sécurité et des possibilités de vérification ?
- **Examinez les accès.** Qui, chez vos prestataires, peut accéder à quoi chez vous ? Supprimez les accès inutiles, limitez les privilèges et assurez-vous de pouvoir tracer les interventions.
- **Vérifiez les engagements.** Les mises à jour, la maintenance, les sauvegardes et la gestion des vulnérabilités sont-elles organisées ?
- **Évaluez vos dépendances.** Que faudrait-il pour poursuivre l'activité sans ce fournisseur ? Existe-t-il une solution de remplacement réaliste ?

Et si vous êtes côté projet, maître d'ouvrage ou maître d'œuvre ? N'attendez pas l'exploitation : les dépendances n'ont jamais été aussi faciles à lister qu'au moment où vous êtes en train de les créer.

Et enfin, posez-vous cette question : si ce prestataire disparaissait demain matin, que ferions-nous ?

Si la réponse est « on ne sait pas », vous savez par où commencer.

## Conclusion

La plupart des fournisseurs et prestataires sont des partenaires honnêtes et compétents, sans lesquels vous ne pourriez tout simplement pas fonctionner.

Mais c'est justement parce que vous dépendez d'eux que vous devez les connaître, les choisir avec soin, suivre l'évolution des risques et savoir comment vous en passer le jour où il le faudra.

La gestion des tiers ne consiste pas à se méfier de tout le monde. Elle consiste à ne pas découvrir ses dépendances le jour où elles deviennent un problème.

## Annexe : deux exemples de responsabilité non déléguée

Une précision d'abord : ces deux affaires ne relèvent pas de l'environnement industriel. CyberRepères étant spécialisé en cybersécurité industrielle, elles ne sont pas citées comme des cas du secteur, mais uniquement pour illustrer un principe qui, lui, s'applique partout — et donc aussi à vos installations.

**Target (2013).** Des attaquants sont entrés dans le réseau de la chaîne de distribution américaine par les identifiants volés de Fazio Mechanical Services, un prestataire frigoristique et CVC. La porte d'entrée était un frigoriste. De ce point d'appui, ils ont atteint les systèmes de caisse et prélevé environ 40 millions de numéros de cartes bancaires, ainsi que les données personnelles de quelque 70 millions de clients. En 2017, Target a accepté un règlement de 18,5 millions de dollars avec 47 États américains, pour un coût total de l'incident supérieur à 200 millions de dollars. Le point important ici : c'est Target qui a été reconnu responsable de l'insuffisance de ses contrôles sur ses prestataires — pas le prestataire.

**Morgan Stanley (2022).** La banque a confié, dès 2015, la mise au rebut de milliers de disques durs et de serveurs à une entreprise de déménagement et de stockage qui n'avait aucune compétence en destruction de données — sans exiger d'attestation de destruction ni vérifier son travail. Le matériel a fini vendu aux enchères en ligne, avec des données de clients non chiffrées : environ 15 millions de clients concernés, des serveurs perdus de vue, et 35 millions de dollars d'amende infligée par le régulateur américain des marchés financiers. Là encore, c'est la banque qui a été sanctionnée, pas le déménageur.

Ces affaires concernent la distribution et la banque aux USA. Mais la logique est universelle : celui qui confie demeure responsable de ceux qu'il choisit et de la surveillance qu'il exerce. Le RGPD, comme la directive NIS2, posent le même principe en Europe — externaliser ne libère de rien. Et l'attaque d'octobre 2026 contre les installations frigorifiques des supermarchés français, si elle doit un jour s'expliquer devant un juge, posera très probablement les mêmes questions : qui connaissait les dépendances, qui devait migrer les équipements en fin de vie, qui devait relayer les alertes ?

---
layout: default
title: "Plan D'Assurance Sécurité"
description: "le PAS c'est quoi ? son but ? quand doit-on le mettre en œuvre ? comment s'y prendre ?..."
category: "comprendre"
tags:
  - Supply-chain
  - IT
  - ICS
  - Assurance Cybersécurité
  - Gestions des risques
  - cybersécurité industrielle
  - Gouvernance
date: 2026-08-21
revision: 2026-08-21
chapter: "Documentation"
order: 40
comments: true
---

**Qu’est-ce qu’un Plan d’Assurance Sécurité (PAS) ?**
Le PAS est un document contractuel qui décrit l’ensemble des dispositions spécifiques qu’un prestataire s’engage à mettre en œuvre pour garantir le respect des exigences de sécurité du donneur d’ordres (client).

Il sert de :

- Cadre de réponse pour les candidats à un appel d’offres, permettant d’évaluer la maturité cyber du soumissionnaire et comparer les offres.
- Annexe au contrat une fois le prestataire retenu, se complète les clauses génériques de sécurité du prestataire.
- Outil de pilotage pour suivre l’application des mesures de sécurité pendant toute la durée du contrat.

**Le PAS : une démarche transverse, pas uniquement un sujet de cybersécurité**

Le Plan d'Assurance Sécurité n'est pas uniquement un sujet de cybersécurité. Sa préparation et son suivi impliquent plusieurs fonctions de votre organisation : cybersécurité, achats, juridique, métiers, DPO lorsque cela est pertinent, responsables des systèmes concernés, etc.

La cybersécurité peut naturellement piloter ou coordonner la démarche... Mais pour que le dispositif soit réellement efficace, les différents acteurs doivent être associés dès le début et comprendre leur rôle.

Le PAS intervient sur plusieurs sujets : contractualisation, responsabilités, engagements du prestataire, protection des données, gestion des risques, exigences réglementaires, modalités d'audit et de contrôle, etc.

Mon conseil : ne faites pas du PAS un document « de la Cyber ». Faites-en une démarche collective. Impliquez les juristes et les acheteurs dès la préparation de la consultation, associez les métiers et les responsables des systèmes concernés, et faites intervenir le DPO lorsque la prestation implique des données à caractère personnel.

Enfin, prenez le temps de sensibiliser et, lorsque nécessaire, de former les personnes amenées à utiliser cette démarche. Un PAS n'est réellement efficace que si ceux qui l'élaborent, le négocient, l'approuvent et le suivent en comprennent les objectifs et savent comment l'utiliser.

**Dans quel cas faut-il réaliser un PAS ?**

Le PAS est nécessaire lorsque la prestation introduit une exposition ou un risque qu'il faut formaliser et maîtriser (infogérance, d'intégration d'un système etc) :
Autrement dit, le PAS devient nécessaire dès que la prestation (que l'on s'apprête à signer) peut devenir vecteur d'une compromission.

Imaginons maintenant que deux sociétés d'un même groupe profitent d'une même gouvernance cyber parce qu'elle partage un même RSSI, on peut considérer que le PAS n'est pas obligatoire parce que 
- les deux entités sont soumises au même référentiel de sécurité (même PSSI, même RSSI etc)
- les exigences applicables sont effectivement équivalentes
- les responsabilités sont clairement définies
- les mesures de sécurité sont effectivement communes ou alignées
- la prestation ne crée pas une exposition supplémentaire significative
- Aucun texte ou contrat applicable n'impose explicitement un PAS

Attention, ceci peut-être reconsidéré lorsque la prestation donne accès à un système présentant un niveau de sensibilité ou de criticité supérieur à celui habituellement couvert par le prestataire. Dans ce cas, un PAS peut être nécessaire afin de formaliser les exigences de sécurité spécifiques applicables à cette intervention.

**Textes, cadres réglementaires et Normes**

Le Plan d’Assurance Sécurité (PAS) est abordé dans plusieurs référentiels et cadres de cybersécurité en France (oui, le terme « Plan d’Assurance Sécurité » est un terme principalement utilisé dans le contexte français).

L’ANSSI aborde le PAS dans son **Guide de l’externalisation des systèmes d’information**, où elle le présente comme un document permettant de préciser les dispositions de sécurité applicables à une prestation d’externalisation et les engagements du prestataire. Le PAS est également présent dans le référentiel ANSSI relatif aux prestataires d’intégration et de maintenance de systèmes industriels.

Le CLUSIF aborde également le PAS dans son Guide de la cybersécurité des systèmes industriels, en lien avec les prestations réalisées sur les systèmes industriels.

Il convient de distinguer les référentiels et les guides par rapport des textes réglementaires : ni l’ANSSI, dans ses guides, ni la directive NIS2 imposent une obligation de réaliser un PAS pour tel ou tel prestation informatique.

La directive NIS2 ne mentionne d'ailleurs pas le « Plan d’Assurance Sécurité ». Elle impose en revanche aux entités de maîtriser les risques liés à leur chaîne d’approvisionnement et à leurs relations avec leurs fournisseurs et prestataires. Le règlement d’exécution (UE) 2024/2690 précise notamment les exigences relatives à la sécurité de la chaîne d’approvisionnement et à la prise en compte de la cybersécurité dans les relations contractuelles.

Le PAS est un moyen permettant de formaliser et de démontrer la prise en compte de ces exigences.

*Pour ce qui concerne les Normes :*

L’IEC 62443-2-4:2023 ne prescrit pas un document intitulé « Plan d’Assurance Sécurité » — et oui vu que le terme "PAS" est une terminologie française.

Pour les prestations d’intégration et de maintenance d’IACS, la norme IEC 62443-2-4 définit en revanche un Security Program pour les fournisseurs de services et prévoit que les exigences et responsabilités de sécurité du prestataire soient définies ou référencées dans les documents de consultation et dans l’accord contractuel avec *l’Asset Owner*.

La norme prévoit ainsi une démarche de définition, négociation et contractualisation des exigences de cybersécurité avant le début de la prestation.

Dans ce contexte, un PAS peut constituer un moyen documentaire de matérialiser cette démarche. 

*Dans la série IEC 62443, le terme Asset Owner est utilisé pour désigner l'acteur responsable de l'installation ou du système. Les notions françaises de MOA/MOE ne correspondent pas directement à la terminologie employée par la norme. Je ferai une page dédiée pour décrire ceci.*


**Quand faire le PAS ?**

Le PAS doit être préparé en amont de la contractualisation de la prestation, et intégré dès la phase de consultation des prestataires.

L'objectif est de ne pas attendre que le prestataire soit choisi pour définir les exigences de sécurité. Celles-ci doivent d'abord être déterminées par le donneur d'ordre en fonction des risques liés à la prestation, puis communiquées aux soumissionnaires.

Le PAS constitue alors la réponse du prestataire aux exigences de sécurité du donneur d'ordre. L'ANSSI recommande ainsi de demander le PAS dès l'appel d'offres ; il sert notamment de cadre de réponse pour comparer les offres et, après sélection du prestataire, est annexé au contrat.
- Il est demandé dans l’appel d’offres et doit être fourni par les candidats en réponse à la consultation.
- Une fois le prestataire choisi, le PAS est annexé au contrat et devient alors un engagement contractuel du prestataire.

C'est un document vivant : 

Le PAS ne doit pas être considéré comme un document figé produit uniquement au démarrage de la prestation. Le guide ANSSI prévoit la possibilité de le faire évoluer pendant l'exécution du marché, notamment lorsque le système, son environnement ou le périmètre de l'opération évolue.

**Déroulement**

<div class="mermaid">
flowchart TD
    A["1 - Analyse du besoin et des risques"]
    B["2 - Définition des exigences de sécurité"]
    C["3 - Élaboration du canevas PAS"]
    subgraph CONSULTATION["Phase de consultation"]
        D["4 - PAS soumis aux candidats"]
        E["5 - Retour, Analyse et négociation des réponses"]
        F["6 - Analyse et comparaison des réponses"]
        G["7 - Négociation et levée des écarts"]
    end
    H["8 - Choix du prestataire"]
    subgraph CONTRACTUALISATION["Contractualisation"]
        I["8 - PAS finalisé et Annexé au Contrat"]
    end
    I["9 - PAS finalisé et Annexé au Contrat"]
    J["10 - Suivi et évolution du PAS pendant la prestation"]

    A --> B
    B -->|"1ère itération"| C
    B -->|"itérations suivantes"| G
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> |"1ère itération"| I
    I --> J
    J -.->|"Évolution du besoin / du risque"| A
    G --> |"itérations suivantes"| J
</div>


## Les étapes de mise en oeuvre ##

## Étape 1 - Analyse de la prestation et des risques ##

Avant de rédiger le PAS, le commanditaire doit déterminer ce que la prestation va permettre au prestataire de faire, sur quels systèmes, avec quelles données et avec quel niveau d'accès.

L'objectif n'est pas nécessairement de réaliser une nouvelle analyse de risques complète : il s'agit d'identifier les risques introduits ou aggravés par la prestation afin de déterminer les exigences de cybersécurité qui devront être imposées au prestataire. D'ailleurs si vous avez une analyse de risques c'est le moment de la sortir et de capitaliser dessus.

### 1.1 Cadre de la prestation

Commencer par décrire ce que vous attendez précisément de la prestation :

- Quel est son objet ?

- S'agit-il d'une externalisation, d'une intégration, d'une maintenance, d'un hébergement, d'une télémaintenance, d'une assistance, etc. ?

- Quels systèmes, quelles machines ou quels SI sont concernés ?

- Quelles données sont concernées ?

- Quels environnements sont concernés : chez vous dans vos locaux OT ? dans un environnement de développement chez le prestataire… ?

- Quelle est la durée de la prestation ?

- Le prestataire intervient-il ponctuellement ou de manière permanente ?

- Fait-il appel lui aussi à de la sous-traitance ?

Cette première étape permet déjà de savoir où se situe le risque.

### 1.2 Identifier les accès et capacités du prestataire

C'est probablement le point le plus important pour un PAS. Il faut identifier ce que le prestataire pourra réellement faire :

| Thème | Question à se poser |
|---|---|
| Accès physique | Le prestataire pourra-t-il accéder aux locaux ou équipements ? |
| Accès logique | Disposera-t-il d'un compte sur le SI ? |
| Privilèges | Peut-il disposer de droits administrateur ? |
| Intervenants | Sont-ils dignes de confiance ? |
| Accès distant | Peut-il intervenir depuis l'extérieur ? |
| Données | Peut-il consulter, modifier ou extraire des données ? |
| Configuration | Peut-il modifier la configuration des systèmes ? |
| Logiciels | Va-t-il faire rentrer du logiciel ? Pourra-t-il installer ou mettre à jour ces logiciels ? |
| Matériel | Interviendra-t-il avec ses PC d'entreprise ? |
| Sécurité | Peut-il modifier des mécanismes de sécurité ? |
| Sous-traitance | D'autres acteurs auront-ils les mêmes capacités ? |


Identifier les menaces, vulnérabilités et impacts spécifiques au contexte de l’externalisation ou du projet.
Déterminer les objectifs de sécurité pour rendre les risques acceptables (réduction, transfert, évitement ou acceptation).

### 1.3. Identifier ce qui pourrait être compromis

Il faut ensuite regarder les conséquences possibles d'une compromission du prestataire ou de ses moyens d'intervention. Par exemple :

| Aspect | Conséquence |
|---|---|
|Confidentialité|accès à des informations sensibles <br> extraction de données <br> accès aux secrets ou identifiants.|
|Intégrité|modification de données <br>modification de configurations <br>introduction de logiciels ou de paramètres malveillants.|
|Disponibilité|arrêt d'un système <br>mauvaise configuration <br>interruption d'un service critique.|
|Sûreté / sécurité physique| Dans un contexte industriel, mais aussi dans le biomédical, les aspects liés à la sûreté de fonctionnement peuvent être très prégnants. Il faut donc considérer les conséquences qu'une intervention sur le système de contrôle pourrait avoir sur le procédé ou sur la sûreté de l'installation, y compris les risques indirects ou adjacents. <br> Je vais consacrer une page à l'approche des IEC 62443, mais pour résumer : le niveau de protection à demander au prestataire dépend directement du système et de son contexte.|


### 1.4. Prendre en compte le niveau de sensibilité / criticité

Le PAS ne devrait donc pas être identique pour toutes les prestations.

Il faut notamment identifier :

La criticité du système
La sensibilité des informations
Les fonctions assurées
Les conséquences d'une compromission
Les exigences réglementaires applicables
Les exigences de sécurité déjà définies par l'organisation

On peut alors avoir une logique simple :

Plus le système est critique ou sensible, et plus la prestation donne au fournisseur des capacités importantes, plus les exigences du PAS devront être fortes.


### 1.5. Identifier les exigences déjà applicables

Avant de créer de nouvelles exigences, il faut rechercher celles qui existent déjà.

Par exemple :

exigences réglementaires ;
politique de sécurité de l'organisation ;
exigences contractuelles existantes ;
exigences sectorielles ;
référentiels applicables ;
exigences du système ;
exigences du client final ;
contraintes liées à la localisation ou à la sous-traitance.

Le PAS ne doit pas devenir un document qui réinvente toutes les exigences de cybersécurité de l'organisation. Il doit plutôt décliner celles qui sont pertinentes pour la prestation et le prestataire.

### 1.6. Déterminer le niveau d'exigence attendu

À l'issue de cette analyse, on doit être capable de répondre à une question simple : *Quel niveau de confiance dois-je obtenir de ce prestataire compte tenu de ce que je lui permets de faire ?*

Par exemple :

Prestation faible exposition

Le prestataire :

* n'accède pas au SI ;
* n'accède pas aux données sensibles ;
* n'a pas de privilège particulier.

*Un PAS formel peut être disproportionné.*

Prestation à exposition significative

Le prestataire :

* accède au SI ;
* intervient à distance ;
* manipule des données sensibles ;
* effectue des opérations de maintenance.

*Un PAS devient pertinent.*

Prestation à forte criticité

Le prestataire :

* administre un système critique ;
* dispose d'accès privilégiés ;
* intervient à distance ;
* peut modifier des fonctions de sécurité ;
* intervient sur un système industriel critique.

→ PAS formel + exigences détaillées + preuves + vérification/audit deviennent particulièrement pertinents.

L'analyse du besoin et des risques permet de déterminer ce que le prestataire pourra faire, ce à quoi il pourra accéder et quelles conséquences pourrait avoir une compromission de la prestation. Elle constitue la base permettant de définir les exigences de sécurité qui seront ensuite intégrées au PAS.


## Étape 2 - Définition des exigences de sécurité ##

Une fois le besoin et les risques identifiés, le commanditaire doit définir les exigences de sécurité applicables à la prestation.

Ces exigences doivent être déterminées à partir :

* des risques identifiés lors de l'étape précédente
* de la PSSI et des règles de sécurité internes
* des exigences réglementaires et contractuelles applicables
* des exigences propres au système concerné
* des référentiels ou normes retenus pour la prestation

Le niveau de sécurité ne doit pas être dégradé. Le recours à un prestataire ne doit pas conduire à abaisser le niveau de sécurité attendu par l'organisation. Si la PSSI du commanditaire impose, par exemple, l'authentification multifacteur pour les accès d'administration, cette exigence ne devrait pas disparaître simplement parce que le prestataire fonctionne habituellement avec un autre dispositif.

Au contraire, *les exigences de sécurité doivent être maintenues et, lorsque les risques identifiés le justifient, renforcées* pour tenir compte des spécificités de la prestation.

Le PAS ne sert pas à demander au prestataire « quel niveau de sécurité pouvez-vous fournir ? ». Il sert à formaliser « quel niveau de sécurité est requis et comment allez-vous le respecter ? ».

| Risque / exposition | Exigence pouvant être définie |
|---|---|
|Accès distant au SI|MFA, bastion, restrictions horaires, journalisation
|Accès privilégié|comptes nominatifs, gestion des privilèges, traçabilité
|Accès à des données sensibles|restriction des accès, chiffrement, règles de conservation
|Intervention sur un système critique|procédures renforcées, validation préalable, supervision
|Installation de logiciels|contrôle et validation des composants
|Maintenance|gestion des vulnérabilités et des correctifs
|Sous-traitance | exigences applicables aux sous-traitants
|Intervention sur système industriel | exigences spécifiques OT / IACS

L'objectif est donc d'obtenir un socle d'exigences cohérent avec le niveau de risque, sans créer inutilement des exigences qui ne seraient pas pertinentes pour la prestation.

Les exigences de sécurité constituent le fond du PAS. Le canevas défini à l'étape suivante permettra de structurer la réponse du prestataire et de vérifier, exigence par exigence, la manière dont il prévoit de les satisfaire.


## Étape 3 – Élaboration du canevas du PAS

Une fois les exigences de sécurité définies, il faut déterminer **sous quelle forme le soumissionnaire devra y répondre**.

Le canevas du PAS constitue la **trame attendue du document**. Il définit les chapitres, les sous-chapitres et, si nécessaire, les informations attendues dans chacune des parties. L'objectif est de donner au soumissionnaire une structure claire qu'il devra compléter dans sa réponse.

### Une structure commune pour toutes les réponses

Cette étape peut sembler purement documentaire, mais elle est loin d'être anodine.

Le canevas doit être construit dans l'ordre dans lequel vous souhaitez retrouver les informations dans le PAS final. Par exemple :

| Chapitre | Sujet                              |
| -------- | ---------------------------------- |
| 1        | Présentation de la prestation      |
| 2        | Organisation et responsabilités    |
| 3        | Gestion des accès                  |
| 4        | Protection des données             |
| 5        | Gestion des vulnérabilités         |
| 6        | Gestion des incidents              |
| 7        | Traçabilité et journalisation      |
| 8        | Maintien en condition de sécurité  |
| 9        | Réversibilité et fin de prestation |

L'intérêt est simple : **tous les soumissionnaires répondent aux mêmes sujets au même endroit**.

Lors de l'analyse des offres, vous pourrez ainsi comparer le chapitre 6 d'un soumissionnaire avec le chapitre 6 des autres, le chapitre 7 avec le chapitre 7, etc.

> **Croyez-moi : une bonne structure de PAS vous fera gagner énormément de temps au moment de comparer les réponses.**

À l'inverse, si chaque soumissionnaire est libre de construire son propre document, vous risquez de devoir rechercher les mêmes informations dans plusieurs dizaines de pages, avec des organisations et des niveaux de détail différents.

### Ne pas se limiter à lister les exigences

Le canevas doit bien entendu reprendre les **exigences de sécurité auxquelles le soumissionnaire doit répondre**. Mais il peut être utile d'aller un peu plus loin.

Vous pouvez ajouter directement dans le canevas des **consignes à l'attention de la personne qui devra le remplir** :

* préciser le niveau de détail attendu ;
* indiquer les éléments de preuve à fournir ;
* demander de distinguer les dispositions déjà en place de celles qui seront mises en œuvre ;
* demander d'identifier les éventuels écarts ;
* préciser le format attendu pour certaines réponses ;
* donner des exemples lorsque le sujet peut prêter à interprétation ;
* indiquer explicitement lorsqu'une réponse est obligatoire ou conditionnelle.

L'objectif est de **lever le maximum d'ambiguïtés dès la consultation**.

Chaque doute laissé dans le canevas peut potentiellement se transformer en une question du soumissionnaire, puis en un aller-retour supplémentaire. À l'inverse, quelques indications bien placées peuvent rendre les réponses beaucoup plus homogènes et directement exploitables.

### Le canevas n'est pas le PAS

Il est important de distinguer les deux. Le **canevas** est la structure et le cadre de réponse définis par le commanditaire. Le **PAS** est le document renseigné par le soumissionnaire, puis éventuellement complété, négocié et finalisé avec le prestataire retenu. Le canevas doit donc être suffisamment précis pour guider la réponse, **sans chercher à rédiger à la place du prestataire les dispositions qu'il s'engage à mettre en œuvre**.

> **Mon conseil : ne faites pas seulement un sommaire. Faites un véritable cadre de réponse.**
>
> Plus vous réduirez les ambiguïtés à ce stade, moins vous aurez de questions et d'allers-retours pendant la consultation, et plus les offres seront faciles à comparer.

### Préparer la grille de notation dès cette étape

Un autre point à ne surtout pas négliger : **la grille de notation des réponses doit être préparée en même temps que le canevas du PAS.**

Il ne faut pas attendre d'avoir reçu les réponses des soumissionnaires pour décider de ce qui est important.

Pour chaque exigence ou thème de sécurité, il est utile de déterminer :

* son niveau d'importance ;
* le nombre de points qui lui sont attribués ;
* les éventuels critères permettant de différencier une réponse satisfaisante d'une réponse insuffisante ;
* et surtout, les exigences sur lesquelles **aucun compromis ne pourra être accepté**.

Toutes les exigences ne doivent pas nécessairement avoir le même poids. Une mesure fondamentale pour la sécurité de la prestation doit peser davantage dans l'évaluation qu'une disposition secondaire.

### Identifier les points qui ne seront pas négociables

C'est également le moment de distinguer les exigences pour lesquelles une discussion avec le soumissionnaire sera possible de celles qui constituent de véritables **conditions de sécurité**.

Par exemple, si une exigence est directement liée à un risque majeur identifié lors de l'analyse des risques, il peut être décidé qu'une réponse insuffisante sur ce point sera éliminatoire, ou qu'elle nécessitera impérativement une mesure compensatoire acceptable.

À l'inverse, certaines exigences pourront laisser davantage de place à la proposition du soumissionnaire.

Cette réflexion est particulièrement utile lors de la phase de négociation : **on sait à l'avance sur quels sujets on peut discuter et sur lesquels on ne doit pas baisser le niveau de sécurité.**

> **Mon conseil : définissez vos priorités avant de recevoir les PAS.**
>
> Identifiez les quelques exigences sur lesquelles vous savez déjà qu'aucun consensus ne sera possible si le niveau de sécurité attendu n'est pas atteint. Donnez-leur le poids correspondant dans votre grille de notation.
>
> Cela vous évitera de vous retrouver, au moment de comparer les offres, à négocier à chaud sur des sujets qui auraient dû être considérés comme non négociables dès le départ.

La grille de notation devient ainsi le prolongement naturel de l'analyse des risques : **plus un sujet est critique pour la sécurité de la prestation, plus son importance dans l'évaluation doit être clairement matérialisée.**

### Attention à ce que vous communiquez aux soumissionnaires

Lors de la rédaction du canevas et des exigences de sécurité, il faut également se poser une question simple :

> **Qu'est-ce que le soumissionnaire a réellement besoin de savoir pour répondre à la consultation ?**

Il est nécessaire de communiquer clairement **le niveau de sécurité attendu et les exigences auxquelles la prestation devra répondre**. En revanche, cela ne signifie pas qu'il faut lui dévoiler la manière dont votre propre organisation atteint ce niveau de sécurité.

Par exemple, vous pouvez demander :

> *« Les accès d'administration à la solution devront être protégés par une authentification multifacteur. »*

sans nécessairement expliquer dans le dossier de consultation **quelle solution d'authentification est utilisée par votre organisation, comment elle est architecturée, quels mécanismes internes sont en place ou quelles mesures complémentaires vous avez déployées**.

Cette distinction est particulièrement importante pour les **systèmes sensibles ou critiques**.

Lorsque plusieurs entreprises sont consultées, les informations communiquées dans le cadre de la consultation peuvent potentiellement être vues par plusieurs acteurs. Il faut donc éviter de transformer le dossier de consultation en une description détaillée de votre propre dispositif de cybersécurité.

**Communiquez ce qui est nécessaire pour que le candidat puisse construire sa réponse, mais protégez ce qui relève de votre propre dispositif de défense.**

Lorsque des informations plus sensibles doivent malgré tout être communiquées pour permettre au soumissionnaire de répondre correctement, prévoyez les **canaux et les modalités de partage adaptés au niveau de sensibilité de ces informations**.

> **Mon conseil : exprimez le niveau de sécurité que vous exigez ; ne dévoilez pas inutilement la manière dont vous protégez déjà votre système.**
>
> Le PAS doit permettre au soumissionnaire de démontrer qu'il saura atteindre le niveau de sécurité demandé, pas de lui fournir une cartographie de vos propres défenses.


## Étape 4 – Le PAS soumis aux candidats

À ce stade, **la balle est dans le camp des soumissionnaires**.

Le commanditaire a défini ses exigences de sécurité et fourni un canevas : c'est maintenant au candidat de le renseigner et d'expliquer **comment il compte répondre aux exigences de la prestation**.

Le PAS proposé doit permettre au commanditaire de comprendre notamment :

* quelles dispositions de sécurité seront mises en œuvre ;
* comment elles seront mises en œuvre ;
* qui en aura la responsabilité ;
* quels moyens techniques, organisationnels ou humains seront mobilisés ;
* comment les exigences seront maintenues dans le temps ;
* quels éléments de preuve pourront être fournis ;
* et, le cas échéant, quels écarts ou difficultés ont été identifiés.

Le PAS n'est donc pas simplement une déclaration de conformité du type *« oui, nous respectons l'exigence »*. Le candidat doit donner suffisamment de matière pour permettre au commanditaire d'apprécier la réalité et la pertinence des dispositions proposées.

### Une façon simple d'expliquer l'exercice au soumissionnaire

Imaginez que vous deviez souscrire une assurance auprès d'une compagnie et que vous deviez lui démontrer qu'elle ne prend pas un risque inconsidéré en vous faisant confiance.

Pour accepter de vous assurer, elle va chercher à comprendre votre situation, les risques auxquels vous êtes exposé et surtout les mesures que vous avez mises en place pour les maîtriser.

Pour le PAS, c'est un peu la même logique.

> **L'exercice qui vous est demandé consiste à démontrer au commanditaire qu'il peut vous faire confiance pour réaliser la prestation dans le respect des exigences de sécurité définies.**
>
> Il ne s'agit pas de prétendre que le risque est nul, mais de montrer que les risques relevant de votre prestation sont connus, pris en compte et maîtrisés par des dispositions concrètes.

Cette approche permet également au soumissionnaire de **mettre en valeur sa maturité et son savoir-faire**. Deux candidats peuvent répondre à une même exigence, mais proposer des moyens, une organisation ou des garanties très différents.

Le PAS devient alors un véritable **élément d'appréciation de l'offre**, et pas uniquement un document administratif supplémentaire.

## Étape 5 – Retour, analyse et négociation des réponses

Les PAS sont maintenant retournés par les soumissionnaires. Il est temps de les analyser et de les comparer.

Grâce au **canevas commun** et à la **grille de notation préparée en amont**, l'exercice doit être relativement simple : chaque réponse est évaluée sur les mêmes exigences et selon les mêmes critères.

L'analyse doit notamment permettre d'identifier :

* les exigences pleinement satisfaites ;
* les éventuels écarts ;
* les mesures alternatives proposées ;
* les points nécessitant des précisions ;
* et les exigences qui ne pourront pas faire l'objet d'un compromis.

Cette phase peut donner lieu à des **échanges avec les soumissionnaires afin de clarifier les réponses et de négocier les éventuels écarts**.

Attention toutefois à ne pas transformer la négociation en diminution systématique du niveau de sécurité attendu. Lorsqu'une exigence est liée à un risque important, une solution alternative peut être étudiée, mais elle doit apporter un niveau de maîtrise acceptable.

> Le PAS est un outil de dialogue : il permet d'identifier les écarts avant de choisir le prestataire, plutôt que de les découvrir une fois la prestation commencée.

## Étape 6 – Analyse et comparaison des réponses

Une fois les éventuels échanges et négociations terminés, les réponses peuvent être comparées sur une base commune.

La grille de notation définie en amont permet de comparer objectivement les propositions et de faire ressortir les écarts entre les soumissionnaires.

L'analyse ne doit toutefois pas se limiter au nombre de points obtenus. Il faut également vérifier que les exigences considérées comme essentielles ou non négociables sont effectivement satisfaites.

Le PAS apporte ainsi un éclairage complémentaire aux autres critères de sélection : il permet d'intégrer la capacité du soumissionnaire à maîtriser les risques de cybersécurité dans le choix du prestataire.

## Étape 7 – Négociation et levée des écarts

Les derniers échanges avec les soumissionnaires permettent de **lever les derniers écarts**, de clarifier les engagements et, si nécessaire, de définir les mesures compensatoires acceptables.

Cette phase doit permettre d'arriver à un PAS suffisamment précis pour que les engagements de sécurité du futur prestataire soient clairs avant la contractualisation.

### Ne cherchez pas uniquement le « meilleur » en cybersécurité

Une erreur serait de considérer que le prestataire ayant obtenu la meilleure note cybersécurité doit nécessairement être retenu.

Dans une prestation industrielle, la cybersécurité n'est qu'un des critères de choix. **Les compétences métier, l'expérience industrielle, les compétences en automatisme, les moyens humains, les références, la capacité à intervenir sur le terrain ou encore le retour d'expérience sur des prestations passées** peuvent également être déterminants.

Le rôle du PAS est donc de s'assurer que **chaque candidat atteint le niveau de sécurité attendu**, et de permettre, lorsque c'est nécessaire, de travailler avec lui sur les écarts.

> **Ne négligez pas un candidat uniquement parce que son niveau de maturité cyber est moins élevé.**
>
> Si la prestation est intéressante pour d'autres raisons, utilisez les échanges et la négociation pour chercher à **faire progresser son niveau de sécurité jusqu'au niveau attendu**.
>
> L'objectif n'est pas forcément de retenir le prestataire « le plus cyber », mais de retenir **le prestataire le plus adapté à la prestation, avec un niveau de cybersécurité acceptable et maîtrisé**.

## Étape 8 – Choix du prestataire

Le choix du prestataire dépendra naturellement de la prestation et de l'organisation mise en place pour sélectionner les offres. La cybersécurité n'est d'ailleurs pas toujours représentée autour de la table au moment de la décision finale.

Mon conseil : **soyez présent.**

Même si la décision finale ne vous appartient pas, faites connaître vos analyses, vos réserves et vos éventuels points de vigilance. Cela ne changera peut-être pas le choix final, mais vos remarques auront au moins été formellement portées à la connaissance des décideurs.

Et parfois, cette simple présence fait toute la différence.

> **Si le choix se porte finalement sur une solution ou un prestataire que vous aviez identifié comme présentant un risque, vous pourrez au minimum dire : « J'avais identifié ce point et j'avais fait part de mes réserves. »**

## Étape 9 – PAS finalisé et annexé au contrat

Le prestataire est choisi. Les derniers écarts ont été traités : **le PAS doit maintenant être finalisé et annexé au contrat**.

Cette étape peut sembler évidente, mais elle mérite d'être rappelée, notamment aux équipes **achats et juridiques**. Dans la précipitation qui accompagne parfois la contractualisation, il serait dommage que le PAS, après tout le travail réalisé, ne soit finalement pas intégré aux documents contractuels.

Le PAS devient alors **un engagement contractuel du prestataire**.

> **Mon conseil : vérifiez que la dernière version validée du PAS est bien annexée au contrat avant sa signature.**

## Étape 10 – Suivi et évolution du PAS pendant la prestation

La signature du contrat ne doit surtout pas marquer la fin de la vigilance.

Pendant toute la prestation, il faut **s'assurer que les engagements pris dans le PAS sont effectivement respectés** et que les dispositions prévues sont bien mises en œuvre.

Faites des points réguliers avec le prestataire et n'hésitez pas à vérifier concrètement ce qui est réalisé. Lorsque les activités sont effectuées sur un autre site, notamment pour du développement logiciel, **n'hésitez pas à vous déplacer** si cela est pertinent.

Le PAS doit également évoluer lorsque le besoin, l'architecture, les risques ou le périmètre de la prestation évoluent.

> **Un PAS n'a de valeur que s'il correspond à la réalité.**
>
> Ne vous contentez pas de vérifier qu'il est correctement rempli : **assurez-vous que ce qui est écrit est réellement appliqué.**





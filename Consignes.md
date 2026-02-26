## Test technique – Développeur(se) ETL
### Objectif
Ce test a pour objectif d’évaluer votre capacité à comprendre un besoin métier partiellement défini, à structurer un traitement de données, à formuler des hypothèses pertinentes, à proposer une solution exploitable en production et à justifier vos choix techniques et fonctionnels.

L’accent est mis sur votre réflexion, votre capacité d’analyse et votre communication, plus que sur la seule expertise technique.

---

### Données fournies
Trois fichiers CSV vous seront fournis :
 - `stocks.csv` : niveaux de stock par produit et par site
 - `ventes.csv` : ventes par produit, par site et par date
 - `appros.csv` : approvisionnements par produit, par site et par date

---

### Résultat attendu
Vous devez produire un fichier CSV de sortie contenant une ligne par produit, par site et par semaine, depuis la semaine courante jusqu’à la dernière semaine contenant des données.

Chaque ligne devra contenir au minimum les informations suivantes : l’identifiant du produit, l’identifiant du site, la semaine, le stock de fin de semaine, le total des ventes de la semaine, le total des approvisionnements de la semaine, ainsi qu’un indicateur de couverture.

---

### Règles métier
#### Gestion du stock

Le stock fourni correspond à l’état du stock en début de semaine courante. À partir de cette valeur initiale, vous devez reconstituer l’évolution du stock semaine par semaine en tenant compte des ventes et des approvisionnements.

#### Indicateur de couverture
Vous devez ajouter un indicateur de couverture de stock permettant le pilotage opérationnel des commandes. Cet indicateur doit représenter le nombre de semaines d’exploitation permises par le stock disponible.

La couverture est censée diminuer progressivement avec la consommation et augmenter lors des réapprovisionnements.

Aucune méthode de calcul n’est imposée. Vous êtes attendu sur votre capacité à proposer une approche pertinente pour répondre à un besoin que le client n’arrive pas à définir précisément.

---

### Gestion des zones floues
Certaines règles ne sont volontairement pas entièrement définies. Dans ce contexte, il est attendu que vous fassiez des hypothèses raisonnables, que vous proposiez une première version exploitable, que vous identifiiez les points à valider avec un client et que vous documentiez clairement vos choix.

Cette démarche vise à reproduire une situation réelle de projet.

---

### Livrables attendus

#### Fichier de sortie
Un fichier CSV conforme aux spécifications décrites dans ce document.

#### Code de traitement
Un ou plusieurs fichiers Python permettant de produire le fichier de sortie à partir des fichiers fournis.

Le code devra être structuré de manière à favoriser la maintenabilité, l’évolutivité et la lisibilité. Une attention particulière sera portée au respect des standards, à la séparation des responsabilités et au découpage en briques métier cohérentes.

Les instructions nécessaires à l’exécution devront être fournies.

#### Schéma de base de données
Dans une optique d’exploitation en business intelligence, vous devrez proposer un schéma de base de données PostgreSQL permettant d’exploiter efficacement les résultats et de faciliter la création du tableau illustré par l’image ci dessous.

![tableau](tableau.png)

Ce schéma devra être justifié et accompagné d’une explication des choix de modélisation et des cas d’usage visés.

#### Document explicatif
Un document devra présenter vos choix techniques, vos hypothèses métier, la méthode retenue pour le calcul de la couverture, ainsi que la justification de votre modèle de données.

---

### Durée indicative
Le temps estimé pour réaliser ce test est de trois à cinq heures.

Ce test ne demande pas une expertise technique avancée. Il est avant tout attendu que vous proposiez une solution cohérente, argumentée, exploitable et présentable à un client.


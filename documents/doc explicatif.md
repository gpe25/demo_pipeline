Démo mise en place pipeline de données
==============================

**Objectifs :**  
Produire un fichier CSV de sortie contenant une ligne par produit, par site et par semaine, depuis la semaine courante jusqu’à la dernière semaine contenant des données.

Chaque ligne devra contenir au minimum les informations suivantes : l’identifiant du produit, l’identifiant du site, la semaine, le stock de fin de semaine, le total des ventes de la semaine, le total des approvisionnements de la semaine, ainsi qu’un indicateur de couverture.


I. Analyse exploratoire *(cf src/tests/ana_expl.ipynb)*
------------

Utilisation d'un notebook pour une analyse rapide des données mises à disposition.  
Utilisation de pandas pour la manipulation des données et itables pour visualitaion dataframe  
Visualisation très sommaire des données avec Seaborn

Objectifs :
- Prise en main des données  
- Définition des actions de transformation / nettoyage à réaliser  
- Analyse des règles métiers à appliquer / valider  

## 1. Stocks
Aucune notion de date, correspond à la valeur initiale (démarrage)

Aucune donnée manquante & aucune ligne dupliquée dans le fichier

**Fonctionnement :**   code article + code site
- 1 article peut être affecté à plusieurs sites  
- Chaque site dispose d’un stock propre, indépendant des autres
*exemples : 835, 930, 1290, ...*  
<span style="color:#4F81BD; font-weight:bold">=> Règle métier à valider avec le client</span>

**Quantité :**  format float
- 97% des quantités de stocks sont entières  
<span style="color:#4F81BD; font-weight:bold">=> Format float à confirmer par le client</span>  
<span style="color:#4F81BD; font-weight:bold">=> Valeurs extrèmes à valider avec le client (plausibles ou erreurs ?)**</span>

**Sites :**
- 5 sites dont 3 avec peu de données et de stocks (encore actifs?)  
<span style="color:#4F81BD; font-weight:bold">=> Choix à valider avec le client (*cf.I.4. champs communs*)</span>
    
**Choix fonctionnels pour démo :**
- Fichier propre, pas d'actions particulières à effectuer
- Conservation fonctionnement code article + code site
- Conservation de l'ensemble des données (postulat : pas de données abérentes)

**Choix techniques pour démo :**
- Conservation du format float pour quantité stocks
- Renommer champs quantite en stock


## 2. Appros
Aucune donnée manquante mais **des lignes dupliquées**  
<span style="color:#4F81BD; font-weight:bold">=> Voir avec le client si normal (cf. fonctionnement)</span> 
*exemple : article 1766 pour Site1 le 07/03/2026*

**Fonctionnement :**  
- Plusieurs appros possibles par jour et par clé article / site  
<span style="color:#4F81BD; font-weight:bold">=> Règle métier à valider avec le client</span>

**Code article :**  format string  
- 1 valeur non numérique (FRAIS3F)  
<span style="color:#4F81BD; font-weight:bold">=> Anomalie potentielle à valider avec le client (impact sur le format commun du champs article)</span>

**Sites :**  
- 3 sites dont 1 avec très peu d'articles approvisionnés  
<span style="color:#4F81BD; font-weight:bold">=> Choix à valider avec le client (*cf.I.4. champs communs*)</span>

**Quantité :**  
- 2 valeurs extrèmes correspondant à des lignes doublonnées  
<span style="color:#4F81BD; font-weight:bold">=> contrôle à effectuer avec le client / dépendant du choix sur les données dupliquées</span>

**Choix fonctionnels pour démo :**
- Conservation des doublons (même commande passée à plusieurs fournisseurs ?)
- Agrégation des approvisionnements par jour et par clé article / site 

**Choix techniques pour démo :**  
- Modification format pour champs [date] (str -> datetime)
- Modification format pour champs [code_article] (str -> int64) avec suppression 'anomalie'
    - *pour les 2 autres sources, le code article est numérique*
    - *1 seule valeur alphanumérique isolée*
    - *préferer les ID numériques aux ID String quand pas d'impact métier*
- Renommer champs quantite en appros


## 3. Ventes
Aucune donnée manquante & aucune ligne dupliquée dans le fichier

**Fonctionnement :**  
- 1 seule ligne par jour et par clé article / site  
<span style="color:#4F81BD; font-weight:bold">=> Règle métier à confirmer avec le client</span>

**Choix fonctionnels pour démo :**
- Fichier propre, pas d'actions particulières à effectuer

**Choix techniques pour démo :**
- Modification format pour champs [date] (str -> datetime)
- Conservation du format float pour quantité ventes
- Renommer champs quantite en ventes


## 4. Champs communs

**Sites :**

![Concordance site](./concordance_sites.JPG "Concordance sites")

Seuls 2 sites sont communs aux stocks / achats / ventes
<span style="color:#4F81BD; font-weight:bold">=> Choix à valider avec le client (sites inactifs? erreur extraction?)</span>

**Articles :** pour les sites communs aux stocks / achats / ventes
- Seul 38% des articles sur le site 1 sont présents dans les 3 sources
- Aucun article pour le site 3 n'est présent  
<span style="color:#4F81BD; font-weight:bold">=> À creuser et à échanger avec le client</span>

**dates :** pour les sites communs aux stocks / achats / ventes
- Période couverte ventes:
    - date min : 2026-02-09
    - date_max : 2026-12-28
- Période couverte appros:
    - date min : 2026-02-09
    - date_max : 2026-10-20  

La période couverte semble différente selon les sources  
<span style="color:#4F81BD; font-weight:bold">=> À creuser et à échanger avec le client</span>

**Choix fonctionnels pour démo :**
- Intégration uniquement des 2 sites communs aux stocks / achats / ventes (attente retour client)
- Intégration uniquement des périodes communes (attente retour client)

**Choix techniques pour démo :**
- Calcul de la période commune dynamiquement dans le code (vs fichier de paramétrage)


II. Transformation des fichiers sources
------------

**Choix fonctionnels pour démo :**
- Ensemble des choix listés lors de la phase exploratoire

**Choix techniques pour démo :**
- Ensemble des choix listés lors de la phase exploratoire
- Utilisation de pathlib et d'un fichier de config pour la gestion des chemins
- Utilisation d'un fichier de paramètrage
- Utilisation de pandas pour la manipulation des données
- Organisation du projet en dossiers / sous dossiers
- Sauvegarde des données transformées avant fichier de sortie
- 1 fichier .py par traitement (appros / stocks / ventes)
- Ajout de la notion semaine et année pour appros et stocks

**Pour aller + loin :**
- Contrôle(s) automatique(s) à mettre en place ? <span style="color:#4F81BD; font-weight:bold">à définir avec le client</span>
- Gestion des erreurs
- logs et infos traitements


III. Fichier de sortie
------------

**Choix fonctionnels pour démo :**
- Ensemble des choix listés lors de la phase exploratoire

**Choix techniques pour démo :**
- Ensemble des choix listés lors de la phase exploratoire
- Création d'une table 'calendrier' pour être sûr d'avoir l'ensemble des semaines (même celles sans ventes et appros)

**Focus Indicateur de couverture :**  
Métode de calcul :  
Prise en compte des ventes de l'ensemble des semaines précédentes  
Justification :  
Mise en place d'un système très simple et rapidement implémentable pour démarrer.  
**Mais** un modèle de machine learning de type série temporelle ou régression (voir classification si besoin d'un topage de type risque de rupture à x semaines) serait beaucoup + pertinent  
<span style="color:#4F81BD; font-weight:bold">=> à cadrer avec le client</span>

**Pour aller + loin :**
- Contrôle(s) automatique(s) à mettre en place ? <span style="color:#4F81BD; font-weight:bold">à définir avec le client</span>
- Gestion des erreurs
- logs et infos traitements


IV. Schéma BDD
------------

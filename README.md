# demo_pipeline
Exploration d'un jeu de données, hypothèses métiers et démo pipeline d'intégration

Instructions nécessaires à l’exécution
------------

Depuis le terminal :

**1. Cloner le repo**  
git clone https://github.com/gpe25/demo_pipeline.git

**2. Se positionner dans le dossier 'demo_pipeline**  
cd demo_pipeline  

**3. Créer et activer l'environnement virtuel .venv**  
python -m venv .venv --without-pip  
.venv\Scripts\activate  
python -m ensurepip --upgrade

**4. Installer les dépendances**  
python -m pip install -r requirements.txt

**5. Lancer l'execution de la pipeline**  
python -m src.run_pipeline


Document explicatif
------------

Le document explicatif contenant les choix techniques, les hypothèses métier et les différentes méthodes retenues se trouve dans :  
- /documents/doc explicatif/md

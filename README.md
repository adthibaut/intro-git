# intro-to-git
1. Installation git : https://github.com/git-guides/install-git
2. Création dossier dédié : `mkdir github_projects`
3. Ouvrir un terminal dans le dossier
4. Clonage repo distant : git clone https://github.com/adthibaut/intro-to-git.git
5. Installation environement virtuel : python -m venv my_env
6. Activation environnement virtuel : 
    - Windows : .\my_venv\Scripts\activate
    - Mac : source ./venv/bin/activate
    - Linux : source venv/bin/activate
7. Installation gestionnaire dépendances : pip install poetry
8. Initiation poetry : poetry init
9. Remplir les champs, ajouter pandas.
10. On installe les librairies : poetry install 
11. Erreur : ajout de package-mode = false dans tool.poetry
11. Autre façon d'ajouter une librarie : poetry add flask
12. On vire le certif : poetry config certificates.PyPI.cert false
13. En fait pas besoin de la lib, on l'enlève : poetry remove flask
14. 

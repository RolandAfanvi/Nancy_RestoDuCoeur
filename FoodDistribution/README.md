FoodDistributionSystem
Le nom du projet est FoodDistributionSystem. C'est un système de distribution de produits alimentaires basé sur Django.

Fonctionnalités
Gestion des produits : Ajout, modification et suppression de produits alimentaires dans le grand magasin.
Gestion des sites de distribution : Enregistrement des sites de distribution individuels avec leurs coordonnées.
Gestion des commandes : Passage de commandes par les sites de distribution.
Gestion des détails de commande : Ajout et gestion des articles individuels dans une commande.


Installation
Cloner le dépôt du projet :
git clone <URL_DU_REPOS>

Créer un environnement virtuel et l'activer :
shell
Copy
python -m venv env
source env/bin/activate  # Pour Linux/Mac
env\Scripts\activate  # Pour Windows

Installer les dépendances :
pip install -r requirements.txt


Effectuer les migrations de la base de données :
python manage.py migrate


Démarrer le serveur de développement :
python manage.py runserver


Accéder à l'API via http://localhost:8000/api/.


Configuration
Les paramètres de configuration se trouvent dans le fichier core/settings.py.
Vous pouvez configurer l'authentification, l'autorisation et d'autres paramètres spécifiques à votre projet dans ce fichier.

Documentation de l'API
La documentation de l'API est disponible à l'adresse http://localhost:8000/api/docs/. Elle fournit une description détaillée des points de terminaison disponibles et des exemples de requêtes.

Contributions
Les contributions à ce projet sont les bienvenues. Si vous souhaitez contribuer, veuillez ouvrir une pull request sur GitHub.


Auteurs
 - AFANVI Kodjo Roland
Licence
//

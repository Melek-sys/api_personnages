API Personnages – Projet FastAPI
🎯 Objectif
Ce projet a pour but de créer une API REST avec FastAPI permettant de gérer une liste statique de personnages fictifs.

🧱 Fonctionnalités
Affichage des personnages
Un endpoint GET /personnages retourne une liste fixe de personnages.

Sécurisation avec un token
L'accès à l'endpoint est protégé par un token passé dans les en-têtes HTTP. Si le token est invalide, une erreur 401 est renvoyée.

Support CORS
L'API est configurée pour accepter les requêtes CORS, facilitant ainsi l'intégration avec une application frontend.

🚀 Lancer le projet
1. Cloner le dépôt
bash
Copier le code
git clone https://github.com/votre-utilisateur/api-personnages.git
cd api-personnages
2. Installer les dépendances
Assurez-vous d'avoir Python 3.7 ou supérieur installé.

bash
Copier le code
pip install fastapi uvicorn
3. Démarrer le serveur
bash
Copier le code
uvicorn main:app --reload
L'API sera accessible à l'adresse : http://127.0.0.1:8000

🔐 Authentification
Pour accéder à l'endpoint /personnages, vous devez fournir un token dans les en-têtes de la requête.

En-tête requis : token: SECRET123

Si le token est manquant ou incorrect, l'API renverra une erreur 401 Unauthorized.

🔄 Exemple de requête
bash
Copier le code
curl -H "token: SECRET123" http://127.0.0.1:8000/personnages
🌐 Documentation interactive
FastAPI génère automatiquement une documentation interactive accessible à l'adresse :

Swagger UI : http://127.0.0.1:8000/docs

ReDoc : http://127.0.0.1:8000/redoc

📁 Structure du projet
pgsql
Copier le code
api-personnages/
├── main.py
├── personnages.json
├── index.html
├── partie_2/
├── partie_3/
├── partie_4/
└── .gitignore
🧪 Tests
Vous pouvez tester l'API en utilisant des outils comme Postman ou directement via la documentation Swagger fournie par FastAPI.

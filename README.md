L’objectif de ce projet est de fournir une interface (CLI + web simple) permettant :  
- d’interagir avec une IA pour vérifier un nombre et voir s'il est premier,
- d’apprendre à intégrer des modèles d’IA dans une application full-stack.

| Dossier / Fichier         | Description                                      |
|---------------------------|--------------------------------------------------|
| `main.py`                 | Point d’entrée principal de l’application Python |
| `client.py`               | Logique client pour la communication IA          |
| `fonction_ia.py`          | Fonctions utilitaires liées à l’IA               |
| `index.html`              | Interface web minimale                           |
| `script.js`               | Logique front-end                                |
| `styles.css`              | Styles pour l’interface web                      |
| `script.py`, `script2.py` | Scripts Python divers                            |
| `TODO.txt`                | Liste de tâches à réaliser                       |
| `.gitignore`              | Fichiers exclus du suivi Git                     |
| `.idea/`, `__pycache__/`  | Fichiers locaux / compilés                       |





# 📌 Test Consultation Assistant

Bienvenue dans le projet **Test Consultation Assistant** !  
Ce dépôt contient une application d’assistant de consultation basée sur une IA (ou prototype d’apprentissage), mêlant Python, JavaScript et HTML/CSS pour interagir avec un modèle IA.

## 🚀 Objectif

L’objectif de ce projet est de fournir une interface (CLI + web simple) permettant :  
- d’interagir avec une IA pour répondre à des questions ou simuler une consultation,
- d’expérimenter avec des fonctions IA personnalisées,
- d’apprendre à intégrer des modèles d’IA dans une application full-stack.

## 🗂️ Structure du projet

| Dossier / Fichier      | Description |
|------------------------|-------------|
| `main.py`              | Point d’entrée principal de l’application Python |
| `client.py`            | Logique client pour la communication IA |
| `fonction_ia.py`       | Fonctions utilitaires liées à l’IA |
| `index.html`           | Interface web minimale |
| `script.js`            | Logique front-end |
| `styles.css`           | Styles pour l’interface web |
| `script.py`, `script2.py` | Scripts Python divers |
| `TODO.txt`             | Liste de tâches à réaliser |
| `.gitignore`           | Fichiers exclus du suivi Git |
| `.idea/`, `__pycache__/` | Fichiers locaux / compilés |

## ⚙️ Installation

1. Clone le repo :
   ```bash
   git clone https://github.com/semimatt123/test_consultation_assistant.git
   cd test_consultation_assistant
Crée un environnement virtuel (recommandé) :

python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
Installe les dépendances :

pip install -r requirements.txt
▶️ Utilisation
💻 En mode console
Lance l’application principale :

python main.py
Suis les instructions à l’écran pour interagir avec le modèle IA.

🌐 Interface web
Ouvre index.html dans ton navigateur pour :

poser des questions,

afficher les réponses générées par l’IA,

tester l’intégration frontend/backend.

🧠 Fonctionnalités
✔ Réponses IA basiques
✔ Interface console
✔ Prototype d’interface web
✔ Modularisation IA avec fonction_ia.py

📈 Améliorations futures

Voici quelques idées à ajouter :

🔹 Authentification utilisateur

🔹 Utilisation d’une API IA externe (OpenAI, LemmyAI…)

🔹 Historique des conversations

🔹 Déploiement web (Flask/FastAPI + hébergement)

🔹 Tests automatisés (unit tests / integration)

📌 Contribution

Toutes contributions sont les bienvenues !

Fork le projet

Crée une branche pour ta fonctionnalité ou correction (feat/ma-fonction, fix/bug)

Ouvre une pull request

📜 Licence

Ce projet est open-source et libre d’utilisation (à préciser selon ta préférence).
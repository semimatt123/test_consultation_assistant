Explication de ce projet 

# 📌 Test Consultation Assistant

Bienvenue dans le projet **Test Consultation Assistant** !  
Ce dépôt contient une application d’assistant de consultation basée sur une IA (ou prototype d’apprentissage), mêlant Python, JavaScript et HTML/CSS pour interagir avec un modèle IA.

## 🚀 Objectif

L’objectif de ce projet est de fournir une interface (CLI + web simple) permettant :  
- d’interagir avec une IA pour vérifier si un nombre est premier,
- d’expérimenter avec des fonctions IA personnalisées,


## 🗂️ Structure du projet

| Dossier / Fichier          | Description                                      |
|----------------------------|--------------------------------------------------|
| `main.py`                  | Point d’entrée principal de l’application Python |
| `client.py`                | Logique client pour la communication IA          |
| `fonction_ia.py`           | Fonctions utilitaires liées à l’IA               |
| `index.html`               | Interface web minimale                           |
| `script.js`                | Logique front-end                                |
| `styles.css`               | Styles pour l’interface web                      |
| `script.py`, `script2.py`  | Scripts Python divers                            |
| `TODO.txt`                 | Liste de tâches à réaliser                       |
| `.gitignore`               | Fichiers exclus du suivi Git                     |
| `.idea/`, `__pycache__/`   | Fichiers locaux / compilés                       |

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

Bienvenue dans ce projet Python 🎉  

Ce projet a pour objectif de t’aider à comprendre comment fonctionne :
- un programme Python structuré,
- une séparation des fichiers (modules),
- une petite interface en ligne de commande,
- et une interface web simple (HTML / CSS / JavaScript).

Ce projet est adapté aux **débutants en Python**.

---

# 📚 Objectif du projet

L’application permet :

- d’entrer un nombre
- de vérifier s’il est premier
- de comprendre comment organiser un projet Python en plusieurs fichiers

C’est un projet d’apprentissage pour pratiquer :
- les fonctions
- les modules
- l’importation de fichiers
- la logique conditionnelle
- les bases du full-stack simple

---

# 🗂 Structure du projet

| Fichier | Rôle |
|----------|------|
| `main.py` | Programme principal |
| `fonction_ia.py` | Contient les fonctions (ex : test nombre premier) |
| `client.py` | Gère la communication entre les parties du programme |
| `index.html` | Interface web simple |
| `script.js` | Logique côté navigateur |
| `styles.css` | Mise en page |

---

# ⚙️ Installation (Débutant)

## 1️⃣ Installer Python

Télécharge Python ici :  
https://www.python.org/downloads/

Vérifie l’installation :

```bash
python --version
2️⃣ Télécharger le projet
git clone https://github.com/semimatt123/test_consultation_assistant.git
cd test_consultation_assistant
(Si tu n’as pas Git, tu peux télécharger le projet en ZIP.)

▶️ Lancer le programme
Dans le dossier du projet :

python main.py
Puis suis les instructions dans le terminal.

🧠 Exemple d’apprentissage
Dans fonction_ia.py, tu trouveras par exemple une fonction comme :

def est_premier(nombre):
    ...
Cela te permet d’apprendre :

comment créer une fonction

comment utiliser une boucle for

comment retourner une valeur avec return

🚀 Ce que tu peux améliorer
Quand tu seras plus à l’aise :

Ajouter une gestion des erreurs (try / except)

Ajouter des commentaires plus détaillés

Ajouter des tests unitaires

Transformer le projet en API avec Flask ou FastAPI

Ajouter un historique des calculs

🎯 Pourquoi ce projet est utile pour débuter ?
✅ Il est simple
✅ Il montre comment organiser un projet
✅ Il mélange Python et web
✅ Il permet de pratiquer la logique

👨‍💻 Auteur
Projet réalisé dans un objectif d’apprentissage.

🔹 Utilisation d’une API IA externe (OpenAI, LemmyAI…)

🔹 Historique des conversations

🔹 Déploiement web (Flask/FastAPI + hébergement)

🔹 Tests automatisés (unit tests / integration)

📌 Contribution

Toutes contributions sont les bienvenues !

📜 Licence

Ce projet est open-source et libre d’utilisation (à préciser selon ta préférence).
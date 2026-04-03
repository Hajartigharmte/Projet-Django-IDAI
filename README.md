# 🎓 PreSkool — Système de Gestion Scolaire Django

> Application web complète de gestion d'école développée avec Django (Python).  
> Projet de fin de module — Licence Développement Web Avancé | Back end (Python) | 2025/2026  
> Université Abdelmalek Essaadi — FST Tanger

---

## 📋 Description

**PreSkool** est un système de gestion scolaire multi-applications construit avec Django, suivant l'architecture MVT (Modèle-Vue-Template). Il permet de gérer les étudiants, les enseignants, les départements, les matières, les examens, l'emploi du temps et bien plus encore, avec un système d'authentification basé sur les rôles.

---

## ✨ Fonctionnalités

- 👨‍🎓 **Gestion des Étudiants** — CRUD complet (ajout, liste, détail, modification, suppression) avec gestion des parents (OneToOneField).
- 👩‍🏫 **Gestion des Enseignants** — CRUD complet avec profil détaillé
- 🏢 **Départements** — Création et attribution des enseignants aux départements
- 📚 **Matières (Subjects)** — Lien avec départements et enseignants
- 📅 **Emploi du temps (Time Table)** — Planification hebdomadaire
- 📝 **Examens (Exam List)** — Planification et saisie des résultats
- 🎉 **Jours Fériés (Holidays)** — Calendrier des congés de l'établissement
- 🔐 **Authentification personnalisée** — Inscription, connexion, déconnexion avec rôles différenciés (Admin / Enseignant / Étudiant)
- 🛡️ **Interface d'administration Django** — Gestion complète des données

---

## 🏗️ Architecture du projet

```
school/
├── manage.py
├── requirements.txt
├── school/                  # Configuration principale du projet
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── faculty/                 # Application tableau de bord
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── student/                 # Application gestion des étudiants
│   ├── models.py            # Parent + Student (OneToOneField)
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── home_auth/               # Application authentification
│   ├── models.py            # CustomUser (AbstractUser + rôles)
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── static/
│   └── assets/              # CSS, JS, images (Bootstrap/PreSkool)
└── templates/               # Templates HTML
    ├── authentication/
    └── students/
```

---

## ⚙️ Installation et lancement

### Prérequis

- Python 3.10+
- pip
- Git

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/Hajartigharmte/Projet-Django-IDAI.git
cd Projet-Django-IDAI

# 2. Créer et activer l'environnement virtuel
python -m venv monenv

# Windows
monenv\Scripts\activate

# macOS / Linux
source monenv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 5. Créer un super-utilisateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

Accéder à l'application :
- 🌐 Application : http://localhost:8000
- 🔧 Administration : http://localhost:8000/admin/

---

## 👤 Comptes de test

| Rôle | Identifiant | Mot de passe |
|------|-------------|--------------|
| Administrateur | hajar | hajar123 |
| Enseignant | issrae@gmail.com | idai2026 |
| Étudiant | ali@gmail.com | idai2026 |

> ℹ️ Vous pouvez créer ces comptes via l'interface d'administration ou via la page d'inscription en choisissant le rôle approprié.

---

## 🎬 Démonstration vidéo

▶️ **[https://youtu.be/dAhqwy86fpk]**

> La vidéo présente : connexion avec les 3 types de comptes, gestion des étudiants/enseignants/départements, emploi du temps, examens et jours fériés.
> 1er connexion c est pour admin-interface
> 2eme connexion c est pour student-interface
> 3eme conexion est pour teacher-interface

---

## 🗄️ Modèles de données principaux

### `Student` (student/models.py)
- Informations personnelles (prénom, nom, date de naissance, genre, classe…)
- Lien `OneToOneField` vers `Parent`
- Photo de profil (`ImageField`)

### `Parent` (student/models.py)
- Informations père et mère (nom, téléphone, email, occupation)
- Adresses

### `CustomUser` (home_auth/models.py)
- Étend `AbstractUser` de Django
- Champs booléens : `is_student`, `is_teacher`, `is_admin`

---

## 🔗 URLs principales

| URL | Description |
|-----|-------------|
| `/` | Page de connexion |
| `/dashboard/` | Tableau de bord |
| `/student/` | Liste des étudiants |
| `/student/add/` | Ajouter un étudiant |
| `/authentication/signup/` | Inscription |
| `/authentication/login/` | Connexion |
| `/authentication/logout/` | Déconnexion |
| `/admin/` | Interface d'administration |

---

## 🛠️ Technologies utilisées

| Technologie | Version | Usage |
|-------------|---------|-------|
| Python | 3.10+ | Langage principal |
| Django | 4.x | Framework web |
| SQLite | — | Base de données (défaut) |
| Bootstrap | 5 | Interface utilisateur (template PreSkool) |
| Pillow | — | Gestion des images |

---

## 👥 Auteurs

Projet réalisé en binôme dans le cadre du module **Développement Web Avancé — Back end (Python)** :

- **Hajar Tigharmte**
- **Israe Ararou**

Encadrante : **Prof. Sara AHSAIN**

---

## 📄 Licence

Projet académique — Université Abdelmalek Essaadi, FST Tanger | 2025/2026

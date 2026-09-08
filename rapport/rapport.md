# Rapport complet du projet Portfolio

**Date du rapport :** 08 septembre 2026
**Technologie principale :** Django (Python)

---

## 1. Vue d'ensemble

Le projet **portfolio** est une application web construite avec le framework **Django 6.1.1**. Il s'agit d'un site de portfolio personnel qui, pour l'instant, se trouve encore **au tout début de son développement** : seuls le squelette du projet et les applications vides ont été créés. Aucune fonctionnalité métier n'est encore implémentée.

---

## 2. Structure générale du projet

```
portfolio/
├── .env                  # Variables d'environnement (clé secrète, debug)
├── .env.example          # Exemple de configuration à copier
├── .gitignore            # Fichiers/dossiers ignorés par Git
├── manage.py             # Point d'entrée de gestion Django
├── requirements.txt      # Dépendances Python
├── db.sqlite3            # Base de données SQLite (vide)
├── config/               # Configuration du projet (settings, urls, asgi, wsgi)
├── blog/                 # Application "blog"
├── compte/               # Application "compte"
├── contact/              # Application "contact"
├── portfolio/            # Application "portfolio" (éponyme)
├── imagescomplet/        # Dossier d'images brutes
└── rapport/              # Documentation et rapports
```

---

## 3. Fichiers de configuration

### 3.1 `manage.py`
Point d'entrée principal de Django. Il pointe vers le module de configuration **`portfolio.settings`**.

### 3.2 `requirements.txt`
Liste des dépendances Python installées :

| Paquet | Version | Rôle |
|--------|---------|------|
| asgiref | 3.12.1 | Support ASGI pour Django |
| Django | 6.1.1 | Framework web principal |
| gunicorn | 26.2.0 | Serveur WSGI de production |
| sqlparse | 0.6.0 | Analyseur SQL (utilisé par les migrations) |
| tzdata | 2026.3 | Données de fuseaux horaires |
| whitenoise | 6.12.0 | Servir les fichiers statiques en production |

### 3.3 `.env` et `.env.example`
Les variables d'environnement contiennent actuellement :
- `SECRET_KEY` : clé secrète (valeur par défaut de développement non sécurisée)
- `DEBUG` : réglé sur `True` (mode développement)

> ⚠️ **Attention :** Les fichiers `.env` **ne sont pas réellement utilisés** par `settings.py` (aucun `python-dotenv` ou `os.environ` n'est chargé pour les lire).

### 3.4 `.gitignore`
Ignore les éléments suivants : dossier virtuel `.venv/`, `__pycache__/`, fichiers `*.pyc`, base de données `db.sqlite3`, fichiers `.env`, dossier `media/`, `staticfiles/`, `.vscode/`, `.idea/`, et les fichiers `*.log`.

---

## 4. Dossier `config/` (configuration du projet)

Ce dossier contient les fichiers de configuration générés par `django-admin startproject` :

| Fichier | Contenu |
|---------|---------|
| `settings.py` | Paramètres globaux du projet (voir section 4.1) |
| `urls.py` | Routage des URLs (voir section 4.2) |
| `asgi.py` | Configuration ASGI (point d'entrée serveur asynchrone) |
| `wsgi.py` | Configuration WSGI (point d'entrée serveur synchrone) |

### 4.1 `settings.py` — Paramètres actuels

- **`SECRET_KEY`** : `'django-insecure-*kfb7t9ms!...'` (valeur de développement, non sécurisée, à changer en production)
- **`DEBUG`** : `True` (mode développement actif)
- **`ALLOWED_HOSTS`** : `[]` (vide — à configurer pour la production)
- **`INSTALLED_APPS`** : uniquement les applications Django par défaut :
  - `django.contrib.admin`
  - `django.contrib.auth`
  - `django.contrib.contenttypes`
  - `django.contrib.sessions`
  - `django.contrib.messages`
  - `django.contrib.staticfiles`
- **`DATABASES`** : SQLite3 avec fichier `db.sqlite3` à la racine
- **`LANGUAGE_CODE`** : `en-us`
- **`TIME_ZONE`** : `UTC`
- **`STATIC_URL`** : `'static/'`

### 4.2 `urls.py` — Routage actuel

Uniquement l'URL d'administration par défaut :
```
/admin/  →  site d'administration Django
```

---

## 5. Les applications Django

Le projet contient **4 applications** (`blog`, `compte`, `contact`, `portfolio`). **Toutes sont encore vides** : elles ne contiennent que les fichiers générés par défaut (`models.py`, `views.py`, `admin.py`, `tests.py`, `apps.py`, `migrations/`), sans aucune logique métier.

### 5.1 Application `blog`
- **`apps.py`** : classe `BlogConfig` avec `name = 'blog'`
- **Fichiers vides** : `models.py`, `views.py`, `admin.py`, `tests.py`
- **Dossiers** : `migrations/`, `static/blog/{css,images,js}/`, `templates/blog/`

### 5.2 Application `compte`
- **`apps.py`** : classe `CompteConfig` avec `name = 'compte'`
- **Fichiers vides** : `models.py`, `views.py`, `admin.py`, `tests.py`
- **Dossiers** : `migrations/`, `static/compte/{css,images,js}/`, `templates/compte/`

### 5.3 Application `contact`
- **`apps.py`** : classe `ContactConfig` avec `name = 'contact'`
- **Fichiers vides** : `models.py`, `views.py`, `admin.py`, `tests.py`
- **Dossiers** : `migrations/`, `static/contact/{css,images,js}/`, `templates/contact/`

### 5.4 Application `portfolio`
- **`apps.py`** : classe `PortfolioConfig` avec `name = 'portfolio'`
- **Fichiers vides** : `models.py`, `views.py`, `admin.py`, `tests.py`
- **Dossiers** : `migrations/`, `static/portfolio/{css,images,js}/`, `templates/portfolio/`

> ℹ️ **Convention de nommage** : chaque application possède déjà ses dossiers `static/<app>/{css,images,js}` et `templates/<app>/`, conformément aux bonnes pratiques Django.

---

## 6. Ressources et médias

### 6.1 Dossier `imagescomplet/`
Contient une image :
- `WhatsApp Image 2026-09-08 at 01.41.12.jpeg` (~77 Ko)

Il s'agit probablement d'images brutes à destination du portfolio (photos de profil, projets, etc.).

---

## 7. Base de données

- **Type** : SQLite (fichier `db.sqlite3` à la racine)
- **État** : vide (0 octet) — aucune migration n'a encore été appliquée
- **Tables** : aucune table métier créée

---

## 8. Points à corriger / améliorations recommandées

### ⚠️ Problèmes identifiés

1. **Incohérence du nom de module de configuration** : le dossier s'appelle `config/`, mais `manage.py`, `settings.py`, `asgi.py` et `wsgi.py` référencent `portfolio.settings`, `portfolio.urls` et `portfolio.wsgi.application`. Le projet risque de ne **pas démarrer** tant que ce n'est pas corrigé.

2. **Applications non enregistrées** : les applications `blog`, `compte`, `contact`, `portfolio` ne sont **pas ajoutées à `INSTALLED_APPS`** dans `settings.py`. Elles ne seront donc pas prises en compte par Django (ni migrations, ni modèles, ni apps).

3. **`.env` non chargé** : les variables d'environnement ne sont pas lues par `settings.py`. Les valeurs comme `DEBUG` ou `SECRET_KEY` ne proviennent pas réellement du fichier `.env`.

4. **Clé secrète non sécurisée** : une clé par défaut de développement est utilisée (`django-insecure-...`).

### 🔧 Prochaines étapes recommandées

1. Corriger l'incohérence du module de configuration (`config` vs `portfolio`).
2. Ajouter les 4 applications à `INSTALLED_APPS`.
3. Activer le chargement de `.env` (via `python-dotenv` ou `os.environ`).
4. Écrire les modèles métier (articles de blog, projets du portfolio, formulaire de contact, comptes utilisateurs...).
5. Créer et appliquer les migrations initiales.
6. Créer les views, URLs et templates pour chaque application.
7. Développer les pages du portfolio.

---

## 9. Résumé des actifs

| Élément | Détail |
|---------|--------|
| Framework | Django 6.1.1 |
| Base de données | SQLite (vide) |
| Nombre d'applications | 4 (blog, compte, contact, portfolio) |
| Applications implémentées | 0 (toutes vides) |
| Modèles métier | Aucun |
| URLs personnalisées | Aucune (seul /admin/) |
| Templates | Aucun |
| Fichiers statiques | Aucun fichier réel (dossiers vides) |
| Images disponibles | 1 (dans imagescomplet/) |
| Serveur WSGI | gunicorn (en production) |
| Fichiers statiques prod. | whitenoise |

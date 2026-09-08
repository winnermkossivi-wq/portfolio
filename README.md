# WIN'S DEV — Portfolio

Portfolio personnel développé avec **Django** (Python) : accueil animé, projets, blog et contact.

## Fonctionnalités

- Accueil : hero animé, effet reveal au scroll, compteurs dynamiques, carte projets stylisée
- Projets : gestion via l'admin Django (titre, image, stack, liens GitHub/démo)
- Blog : articles publiés, gestion admin
- Contact : formulaire enregistré en base **+ envoi d'email** (SMTP)
- Réseaux sociaux : GitHub, TikTok, Facebook, Instagram, WhatsApp
- Loader, menu mobile circulaire, thème noir & blanc + accents jaunes

## Démarrage en local

```bash
# 1. Créer l'environnement et installer les dépendances
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install -r requirements.txt

# 2. Configurer l'environnement
cp .env.example .env              # puis renseigner SECRET_KEY + SMTP

# 3. Migrer et démarrer
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Va sur `http://127.0.0.1:8000/` et `/admin/` pour l'administration.

## Configuration email (Brevo / SendGrid / Gmail)

Dans `.env` :

```
EMAIL_HOST=smtp-relay.sendinblue.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre_email
EMAIL_HOST_PASSWORD=votre_mot_de_passe_smtp
EMAIL_RECIPIENT=votre_email          # celui qui reçoit les messages
```

## Déploiement (Render)

1. Push le projet sur GitHub (`winnermkossivi-wq`).
2. Sur [Render](https://render.com) : **New → Web Service** ← ton dépôt.
3. Build : `pip install -r requirements.txt`
4. Start command : `gunicorn config.wsgi`
5. Variables d'environnement : copier `.env` (sauf `DEBUG`) + `DEBUG=False`, `ALLOWED_HOSTS=ton-domaine-onrender.com`.

Tableau de bord → onglet **Shell** pour lancer `python manage.py migrate` (et `createsuperuser`).

Statiques servies par whitenoise (`python manage.py collectstatic` automatique au build).

## Licence

Projet personnel — © 2026 WIN'S Dev.
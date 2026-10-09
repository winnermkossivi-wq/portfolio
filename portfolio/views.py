from django.shortcuts import render

from .models import Competence, Projet

LOGOS = {
    'Python': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/python.svg',
    'Django': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/django.svg',
    'HTML': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/html-5.svg',
    'CSS': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/css.svg',
    'JavaScript': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/javascript.svg',
    'Node.js': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/nodejs-icon.svg',
    'GitHub': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/github-icon.svg',
    'Git': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/git-icon.svg',
    'Tailwind CSS': 'https://cdn.jsdelivr.net/gh/gilbarbara/logos@main/logos/tailwindcss-icon.svg',
}


ORDRE_CATEGORIES = ["Backend", "Mobile", "Frontend", "Outils"]


def outils_par_categorie():
    groupes = {}
    for c in Competence.objects.all():
        groupes.setdefault(c.categorie or "Outils", []).append(
            {"nom": c.nom, "niveau": c.niveau}
        )
    categories = [cat for cat in ORDRE_CATEGORIES if cat in groupes]
    categories += [cat for cat in groupes if cat not in ORDRE_CATEGORIES]
    return [{"nom": cat, "outils": groupes[cat]} for cat in categories]


def accueil(request):
    projets = Projet.objects.filter(en_avant=True)
    competences = list(Competence.objects.all())
    for c in competences:
        c.logo = LOGOS.get(c.nom, '')
    return render(request, 'portfolio/accueil.html', {
        'projets': projets,
        'competences': competences,
        'outils_categories': outils_par_categorie(),
    })
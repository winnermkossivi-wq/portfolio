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


def accueil(request):
    projets = Projet.objects.filter(en_avant=True)
    competences = list(Competence.objects.all())
    for c in competences:
        c.logo = LOGOS.get(c.nom, '')
    return render(request, 'portfolio/accueil.html', {
        'projets': projets,
        'competences': competences,
    })
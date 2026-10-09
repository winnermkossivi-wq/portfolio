from django.db import migrations


def remplir_outils(apps, schema_editor):
    Competence = apps.get_model("portfolio", "Competence")
    connus = {
        "Python": ("Backend", 92),
        "Django": ("Backend", 90),
        "Node.js": ("Backend", 78),
        "SQLite": ("Backend", 80),
        "PostgreSQL": ("Backend", 78),
        "HTML": ("Frontend", 95),
        "CSS": ("Frontend", 90),
        "JavaScript": ("Frontend", 85),
        "Git": ("Outils", 88),
        "GitHub": ("Outils", 85),
        "Flutter": ("Mobile", 85),
        "Dart": ("Mobile", 80),
    }
    existants = set()
    for c in Competence.objects.all():
        existants.add(c.nom)
        if c.nom in connus:
            cat, niv = connus[c.nom]
            c.categorie = cat
            c.niveau = niv
            c.save(update_fields=["categorie", "niveau"])
    a_creer = [
        ("Django", "Backend", 90, 1),
        ("SQLite", "Backend", 80, 8),
        ("PostgreSQL", "Backend", 78, 9),
        ("Flutter", "Mobile", 85, 10),
        ("Dart", "Mobile", 80, 11),
    ]
    for nom, cat, niv, ordre in a_creer:
        if nom not in existants:
            Competence.objects.create(nom=nom, categorie=cat, niveau=niv, ordre=ordre)


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_competence_categorie_competence_niveau"),
    ]

    operations = [
        migrations.RunPython(remplir_outils, migrations.RunPython.noop),
    ]

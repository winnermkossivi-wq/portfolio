from django.shortcuts import get_object_or_404, render

from .models import Article


def liste_articles(request):
    articles = Article.objects.filter(publie=True)
    return render(request, 'blog/liste_articles.html', {'articles': articles})


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)
    return render(request, 'blog/detail_article.html', {'article': article})
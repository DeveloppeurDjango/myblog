from django.shortcuts import render
from blog.models import Article


def appadmin(request):
    return render(request, 'contenu.html')

def user_article(request):
    list_articles = Article.objects.filter(user=request.user)
    return render(request, 'my-articles.html', {'list_articles':list_articles})
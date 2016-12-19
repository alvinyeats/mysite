from django.shortcuts import render
from django.http import Http404

from article.models import Article


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, article_id):
    try:
        post = Article.objects.get(id=str(article_id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})



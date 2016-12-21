# -*- coding: utf-8 -*
from django.shortcuts import render
from django.http import Http404

from article.models import Article


def home(request):
    print("test")
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'about_me.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

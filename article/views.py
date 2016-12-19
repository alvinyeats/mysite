from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

from article.models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the article index.")


def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    res_str = ("title = %s, category = %s, date_time = %s, content = %s"
               % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(res_str)


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

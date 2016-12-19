from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

from article.models import Article


def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    res_str = ("title = %s, category = %s, date_time = %s, content = %s"
               % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(res_str)


def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

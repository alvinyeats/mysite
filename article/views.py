from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the article index.")


def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)

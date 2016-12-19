# -*- coding: utf-8 -*

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<my_args>[0-9]+)/$', views.detail, name='detail'),
]
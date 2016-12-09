# -*- coding: utf-8 -*

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse

def hello(request):
    return HttpResponse('Hello Alvin')

def index(request):
    return TemplateResponse(request, 'index.html')


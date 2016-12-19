from django.shortcuts import render,render_to_response
from datetime import datetime

 
def index(request):
    return render_to_response('index.html')


def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})

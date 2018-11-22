from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def about(request):

    templ = loader.get_template('about/index.html')

    return HttpResponse(templ.render(request=request))
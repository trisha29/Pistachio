from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Demographic
# Create your views here.

def home(request):
    demogs= Demographic.objects.all()
    return render(request, 'home.html', {'demogs':demogs})

def respo_code(request, respocode):
    try:
        demog=Demographic.objects.get(id=respocode)
    except Demographic.DoesNotExist:
        raise Http404("Not Found")
    return render(request, 'respo_code.html', {'demog':demog})

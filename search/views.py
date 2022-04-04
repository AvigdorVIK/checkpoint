from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, "search/home.html")

def add(request):
    return render(request, 'search/add.html')

def info(request):
    return(request, 'search/info.html')

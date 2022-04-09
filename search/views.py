from django.http import HttpResponse
from django.shortcuts import render
from search.models import Search


menu = [{"title":'menu', "url_name":'menu'},
        {"title":'add', "url_name":'add'},
        {"title":'info', "url_name":'info'},
        {"title":'exit', "url_name":'exit',}]
posts = Search.objects.all()

def home(request):
    context = {
        "title": 'menu',
         "menu": 'menu' ,
        "posts":'posts',

    }

    return render(request, "search/home.html", context=context)

def add(request):
    return render(request, 'search/add.html', {'posts':posts})

def info(request):
    return render(request, 'search/info.html', {'posts':posts})

def exit(request):
    return render(request, 'search/exit.html', {'post':posts})


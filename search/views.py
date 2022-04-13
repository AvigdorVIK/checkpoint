from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from search import form
from search.form import AddForm
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
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(home)
            except:
                form.add_error(None, 'eror')
    else:
        form = AddForm()
        return render(request, 'search/add.html', {'form':form})







def info(request):
    posts = Search.objects.all()
    return render(request, 'search/info.html', {'posts':posts})

def exit(request):
    return render(request, 'search/exit.html', {'post':posts})


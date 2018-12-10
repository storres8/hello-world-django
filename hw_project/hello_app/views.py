from django.shortcuts import render
from django.http import HttpResponse

def general(request):
    return HttpResponse("<h1>Hello World!</h1>")

def detail(request, id):
    return HttpResponse(f"<h1>Hello, greeting from planet {id}!</h1>")

def help(request):
    help_dict= {'help_page': "YOU'VE REACHED THE HELP PAGE!"}
    return render(request, 'hello_app/index.html', context=help_dict)

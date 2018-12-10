from django.shortcuts import render
from django.http import HttpResponse

def general(request):
    intro={'home_page': "Welcome this page was built using django!"}
    return render(request, 'hello_app/index.html', context=intro)

def detail(request, id):
    return HttpResponse(f"<h1>Hello, greeting from planet {id}!</h1>")

def help(request):
    help_dict= {'help_page': "YOU'VE REACHED THE HELP PAGE!"}
    return render(request, 'hello_app/help.html', context=help_dict)

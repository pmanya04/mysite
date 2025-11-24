 # rebuild test 2

from django.shortcuts import render

def index(request):
    return render(request, "index.html")

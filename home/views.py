 # rebuild test 3

from django.shortcuts import render

def index(request):
    return render(request, "index.html")

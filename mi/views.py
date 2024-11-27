from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hardik(request):
    return HttpResponse("<h1>Hardik is captain of csk</h1>")
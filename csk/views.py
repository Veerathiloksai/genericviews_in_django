from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def rutu(request):
    return HttpResponse("<h1><marquee>Rutu is captain of csk</marquee></h1>")


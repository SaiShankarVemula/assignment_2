from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def disco(request):
    return render(request,'disco.html')

def disco1(request):
    return HttpResponse('<center><h1>DISCO_TECH is a popular dance music characterized by hypnotic rhythm, repetitive lyrics, and electronically produced sounds</h1></center>')
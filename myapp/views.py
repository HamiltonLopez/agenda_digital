from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def hello(request):
    return HttpResponse("<h1>HOLA MUNDO</h1>")


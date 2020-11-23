
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('Home')

def login(request):
  return render(request, 'login.html')

def registro(request):
  return HttpResponse('Registrate')

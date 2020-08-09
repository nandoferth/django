from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def Crud(request):
    return render(request,'accounts/Crud.html')

def Table(request):
    return render(request,'accounts/Table.html')
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login(request):
    
    return render(request,'accounts/Login.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'accounts/Register.html',context)

def home(request):
    return HttpResponse("Home")

def Crud(request):
    return render(request,'accounts/Crud.html')

def Table(request):
    return render(request,'accounts/Table.html')
# Create your views here.

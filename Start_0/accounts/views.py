from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

from .forms import OrdersForm,OrdersProduct,CreationUserForm

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('table')
        else:
            messages.info(request,'file')
    return render(request,'accounts/Login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')
def register(request):
    form = CreationUserForm()
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context={'form':form}
    return render(request,'accounts/Register.html',context)

def home(request):
    return HttpResponse("Home")

def Crud(request):
    return render(request,'accounts/Crud.html')

def CustomerPage(request, pk_test):
    user = Customer.objects.get(name=pk_test)
    product = user.orders_set.filter(status="Pending").count()
    context = {'user':user,'product':product}
    return render(request,'accounts/Customer.html',context)

def Table(request):
    
#-----------------------------------------------------#
    total_ordenes = Orders.objects.all().count()
    total_productos = Product.objects.all().count()
    total_usuarios = Customer.objects.all().count()
    products = Product.objects.all()
    users = Customer.objects.all()
#-----------------------------------------------------#
    formO = OrdersForm()
    #formP = OrdersProduct()
    if request.method == 'POST':
        print('print',request.POST)
        #formP = OrdersProduct(request.POST)
        formO = OrdersForm(request.POST)
        if formO.is_valid():
            formO.save()
            return redirect('/table')
        
    context = {'total_ordenes':total_ordenes,'total_productos':total_productos,
    'total_usuarios':total_usuarios, 'products':products,'users':users,'formO':formO}
    return render(request,'accounts/Table.html',context)



# Create your views here.

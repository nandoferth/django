from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrdersForm

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
    form = OrdersForm()
    if request.method == 'POST':
        print('print',request.POST)
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/table')
    context = {'total_ordenes':total_ordenes,'total_productos':total_productos,
    'total_usuarios':total_usuarios, 'products':products,'users':users,'form':form}
    return render(request,'accounts/Table.html',context)



# Create your views here.

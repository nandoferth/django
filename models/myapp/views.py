from django.shortcuts import render
from .models import *

# Create your views here.
def products(request):
  products = product.objects.all()
  productsSize = product.objects.filter(sizesProduct='S')
  return render(request, 'product.html', {'products':products, 'productsSize':productsSize})

def acounts(request):
  totalAcounts = acount.objects.count()
  acounts = acount.objects.all()
  context = {'totalAcounts':totalAcounts, 'acounts':acounts}
  return render(request, 'acount.html', context)

def acountCustomer(request):
  # user = customer.objects.first()
  user = customer.objects.get(id=2)
  typeUser = user.acount_set.all()
  context = {'typeUser':typeUser}
  return render(request, 'profle.html', context)
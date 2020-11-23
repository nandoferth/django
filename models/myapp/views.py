from django.shortcuts import render
from .models import *

# Create your views here.
def products(request):
  products = product.objects.all()
  return render(request, 'product.html', {'products':products})

def acounts(request):
  totalAcounts = acount.objects.count()
  acounts = acount.objects.all()
  context = {'totalAcounts':totalAcounts, 'acounts':acounts}
  return render(request, 'acount.html', context)
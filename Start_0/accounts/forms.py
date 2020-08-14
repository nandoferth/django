from django.forms import ModelForm
from .models import Orders,Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class OrdersProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

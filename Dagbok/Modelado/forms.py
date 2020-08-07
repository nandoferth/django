from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import BaseModelFormSet
from Modelado.models import *
from .models import Proyecto, Events, UnirseProyecto

class ProyectoFrom(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

class UnirseProyectoForm(ModelForm):
    class Meta:
        model = UnirseProyecto
        fields = ['usuario','proyecto','estatu']
    """estatus=(
        ('Espera','Espera'),
        ('Confirmar','Confirmar'),
        ('Eleminar','Eleminar'),
    )
    usuario = forms.CharField(label="Add New Members", widget=forms.CheckboxSelectMultiple)
    estatu = models.CharField()
    def __init__(self, *args, **kwargs):
        self._pwd = kwargs.pop('pwd', None)
        super(UnirseProyectoForm,self).__init__(*args, **kwargs)
        self.fields['usuario'].queryset = forms.ModelMultipleChoiceField(label="Add New members",
                                                                   widget=forms.CheckboxSelectMultiple,
                                                                   queryset=Proyecto.objects.get(id=self._pwd).usuario.all())"""
        
    #proyecto = forms.ModelChoiceField(EnviarSolicitud.objects.get(id=self._us).agregar_usuario.values_list('name', flat=True) help_text="Company")
    #estatu = forms.ModelChoiceField(queryset=Company.objects.all(), required=False, help_text="Company")

    """def __init__(self, *args, **kwargs):
        self._us = kwargs.pop('us',None)
        super().__init__(*args, **kwargs)
        self.name = forms.ModelMultipleChoiceField( EnviarSolicitud.objects.get(id=self._us).agregar_usuario.values_list('name', flat=True)) 
    """

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
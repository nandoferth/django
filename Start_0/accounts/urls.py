
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('crud/', views.Crud),
    path('table/',views.Table),
    path('login/',views.login),
    path('register/',views.register),
]
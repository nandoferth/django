
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('crud/', views.Crud),
    path('table/',views.Table),
    path('login/',views.login),
    path('register/',views.register),
    path('customer/<str:pk_test>/',views.CustomerPage,name="customer"),
]
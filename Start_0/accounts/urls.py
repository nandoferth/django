
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('crud/', views.Crud),
    path('table/',views.Table,name="table"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('register/',views.register,name="register"),
    path('customer/<str:pk_test>/',views.CustomerPage,name="customer"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('table/', views.table_users)
]
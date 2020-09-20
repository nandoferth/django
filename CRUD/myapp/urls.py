from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('table/', views.table_users),
    path('newjob/', views.create_job, name="newJob"),
    path('updatejob/<str:pk>/', views.update_job, name="updateJob"),
]
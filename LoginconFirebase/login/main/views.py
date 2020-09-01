from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializers
from django.contrib.auth.models import User
from rest_framework import permissions
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes=[permissions.IsAuthenticated,]
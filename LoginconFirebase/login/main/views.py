from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializers
from django.contrib.auth.models import User
from rest_framework import permissions
import pyrebase
# Create your views here.

config = {
    'apiKey': "AIzaSyBRnc9-hJdVmdgyl3NIH85kHAaq39PteMM",
    'authDomain': "djangoapp-27012.firebaseapp.com",
    'databaseURL': "https://djangoapp-27012.firebaseio.com",
    'projectId': "djangoapp-27012",
    'storageBucket': "djangoapp-27012.appspot.com",
    'messagingSenderId': "1062530760973",
    'appId': "1:1062530760973:web:12e9c6799c156faf7f3044"

}
firebase = pyrebase.initialize_app(config)  
auth = firebase.auth()

def singIn(request):
    return render(request,"SingIn.html")

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes=[permissions.IsAuthenticated,]

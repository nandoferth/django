from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import User
# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>Home Page %s </body></html>" %now
    return HttpResponse(html)

def table_users(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'templates/table_users.html', context)
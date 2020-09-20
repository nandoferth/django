from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import User, Job
from .forms import JobForm
# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>Home Page %s </body></html>" %now
    return HttpResponse(html)

def table_users(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request, 'accounts/table_users.html', context)

def create_job(request):
    form = JobForm()
    if request.method == 'POST':
        #print(request.POST)
        form = JobForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('http://127.0.0.1:8000/table/')
    context = {'form':form}
    return render(request, 'accounts/createJob.html', context)

def update_job(request,pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/table/')
    context = {'form':form}
    return render(request, 'accounts/createJob.html', context)
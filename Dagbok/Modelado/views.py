from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from Modelado.models import *
from datetime import datetime
from django.http import JsonResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def Iniciar_Sesion(request):
    return render(request,"login.html")

def Registrarse(request):
    form = CreateUserForm()
    if  request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciarsesion')
    context = {'form':form}
    return render(request,"register.html",context)
def Bienvenido(request,pk_test):
    usuario = Usuario.objects.get(id=pk_test)

    proyectos = usuario.proyecto_set.all()
    total_proyectos_personales = proyectos.count() 
    proyectos_espera = usuario.unirseproyecto_set.filter(estatu="Espera")
    proyectos_invita = usuario.unirseproyecto_set.filter(estatu="Confirmar")
    total_proyectos_ivitado = proyectos_invita.count()
    following = usuario.enviarsolicitud.agregar_usuario.all()
    follwerss = usuario.enviarsolicitud.follwers.all()

    context = {'usuario':usuario,'proyectos':proyectos,'total_proyectos_personales':total_proyectos_personales,'proyectos_espera':proyectos_espera,
    'proyectos_invita':proyectos_invita,'total_proyectos_ivitado':total_proyectos_ivitado,'following':following,'follwerss':follwerss}
    return render(request,"index.html",context)

def Profile(request,pk_test):
    usuario = Usuario.objects.get(id=pk_test)
    total_proyectos_personales = usuario.proyecto_set.all().count() 
    total_proyectos_ivitado = usuario.unirseproyecto_set.filter(estatu="Confirmar").count()
    context={'usuario':usuario,'total_proyectos_personales':total_proyectos_personales,'total_proyectos_ivitado':total_proyectos_ivitado}
    return render(request,"Profile.html",context)

def Calendar(request,pk_test):
    proyecto = Proyecto.objects.get(id=pk_test)
    all_events = proyecto.events_set.all()
    context = {
        "events":all_events,
    }
    return render(request,'fullcalendar.html',context)

def Calendar_Personal(request,pk_test):
    
    usuario = Usuario.objects.get(id=pk_test)
    all_events = usuario.events_set.all()
    context = {
        "events":all_events,
    }
    return render(request,'fullcalendar.html',context)

def add_event(request):
    proyecto_name = Proyecto.objects.get(name="Sockets")
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)

def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def Nuevo_Proyecto(request,pk_test):
    usuario = Usuario.objects.get(id=pk_test)
    contxt={'usuario':usuario}
    form = ProyectoFrom(initial={'usuario':usuario})
    if request.method == 'POST':
        #print('Imprimiendo POST',request.POST)
        form = ProyectoFrom(request.POST)
        if  form.is_valid():
            form.save()
            return render(request,"index.html",contxt)

    context = {'form':form}
    return render(request,"FormNewProject.html",context)

def AgregarEvents(request,pk_test):
    proyecto = Proyecto.objects.get(id=pk_test)
    form = EventsForm(initial={'proyecto':proyecto})
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request,"Proyect.html",{'proyect':proyect})
    context = {'form':form}
    return render(request,'FormNewEvents.html',context)

def ActualizarEvents(request,pk_test):
    events = Events.objects.get(id=pk_test)
    form = EventsForm(instance=events)
    if request.method == 'POST':
        form = EventsForm(request.POST,instance=events)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'FormNewEvents.html',context)

def EleminarEvents(request,pk):
    events = Events.objects.get(id=pk)
    if  request.method == "POST":
        events.delete()
        
    context = {'item':events}
    return render (request,"eleminar.html",context)

def Unirse_Proyecto(request,pk_test):
    proyecto = Proyecto.objects.get(id=pk_test)
    form  = UnirseProyectoForm(initial={'proyecto':proyecto})
    if request.method == 'POST':
        form = UnirseProyectoForm(request.POST)
        if  form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request,"FormUnirseProyecto.html",context)

def EleminarUsuario (request,pk):
    events = UnirseProyecto.objects.get(id=pk)
    if  request.method == "POST":
        events.delete()
        
    context = {'item':events}
    return render (request,"eliminarUsuarioProyecto.html",context)
    
def Buscar_Proyecto(request):
    return render(request,"searchproject.html")

def Proyectos(request,pk_test):
    proyecto = Proyecto.objects.get(id=pk_test)

    actividades = proyecto.events_set.all()
    total_actividades = actividades.count() 

    actividades_importantes = actividades.filter(escoge_importancia="important")
    actividades_info = actividades.filter(escoge_importancia="info")

    usuarios = proyecto.unirseproyecto_set.all().filter(estatu="Confirmar")
    usuario_adm = proyecto.usuario.first()

    context = {'proyecto':proyecto,'actividades':actividades,'total_actividades':total_actividades,
    'actividades_importantes':actividades_importantes, 'actividades_info':actividades_info,'usuarios':usuarios,
    'usuario_adm':usuario_adm}
    return render(request,"Proyect.html",context)



#def Registrarse(request):
    #return render(request,"register.html")

from django.urls import path
from Modelado import views

urlpatterns = [
    path('IniciarSesion/',views.Iniciar_Sesion,name="iniciarsesion"),
    path('Registrarse/',views.Registrarse,name="registrarse"),

    path('Bienvenido/<str:pk_test>/',views.Bienvenido, name="bienvenido"),

    path('Profile/<str:pk_test>/',views.Profile,name="profile"),

    path('Calendario/<str:pk_test>/', views.Calendar,name="calendario"),
    path('CalendarioPersonal/<str:pk_test>/', views.Calendar_Personal,name="calendario_personal"),
    path('add_event', views.add_event, name='add_event'),
    path('update', views.update, name='update'),
    path('remove', views.remove, name='remove'),
    path('AgregarEvents/<str:pk_test>',views.AgregarEvents,name="agregarevents"),
    path('ActualizarEvents/<str:pk_test>',views.ActualizarEvents,name="actualizarevents"),
    path('EleminarEvents/<str:pk>',views.EleminarEvents,name="eleminarevents"),

    path('NuevoProyecto/<str:pk_test>/',views.Nuevo_Proyecto,name="nuevoproyecto"),
    path('BuscarProyecto/',views.Buscar_Proyecto,name="buscarproyecto"),
    path('Proyecto/<str:pk_test>/',views.Proyectos,name="proyecto"),
    path('UnirseProyecto/<str:pk_test>/',views.Unirse_Proyecto, name="unirseproyecto"),
    path('EleminarUsProyecto/<str:pk>/',views.EleminarUsuario, name="eleminarusproyecto"),
]
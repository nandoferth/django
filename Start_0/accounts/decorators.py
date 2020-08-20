from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapp_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('')
        else:
            return view_func(redirect, *args, **kwargs)
    return wrapp_func

"""def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('role: ',allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Solo el administrador puede ver esta Pagina')
        return wrapper_func
    return decorator"""
#loginPage -> obtiene el rol del usuario -> admin_only -> mostrara las vistas deacuerod al rol
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        #print('role: ',allowed_roles)
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('home')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function
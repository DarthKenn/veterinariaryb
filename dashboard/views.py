from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def pagina_principal(request):
    if request.user.is_superuser:
        tipo_usuario = 'Administrador'
        enlaces = [
            {'url': '/productos/', 'nombre': 'Gestionar Productos'},
            {'url': '/productos/categorias/', 'nombre': 'Gestionar Categorías'},
        ]
    else:
        tipo_usuario = 'Usuario Normal'
        enlaces = [
            {'url': '/productos/', 'nombre': 'Gestionar Productos'},
        ]

    context = {
        'tipo_usuario': tipo_usuario,
        'enlaces': enlaces,
    }
    return render(request, 'dashboard/principal.html', context)

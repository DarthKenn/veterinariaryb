from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroFormulario

def registro(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroFormulario()
    return render(request, 'gestorUsers/registro.html', {'form': form})


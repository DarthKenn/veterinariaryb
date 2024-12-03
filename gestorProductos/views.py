from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def es_admin(user):
    return user.is_superuser

@login_required
def listar_productos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all() 
    else:
        productos = Producto.objects.filter(creador=request.user) 

    return render(request, 'gestorProductos/lista_productos.html', {'productos': productos})


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creador = request.user 
            producto.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()

    return render(request, 'gestorProductos/crear_producto.html', {'form': form})


@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)


    if request.user != producto.creador and not request.user.is_superuser:
        return redirect('listar_productos') 

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'gestorProductos/editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    
    if request.user != producto.creador and not request.user.is_superuser:
        return redirect('listar_productos') 

    producto.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('listar_productos')

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.all()  
    return render(request, 'gestorProductos/lista_categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_categorias')  
    else:
        form = CategoriaForm()
    
    return render(request, 'gestorProductos/crear_categoria.html', {'form': form})

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save() 
            return redirect('listar_categorias')  
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'gestorProductos/editar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete() 
    return redirect('listar_categorias') 



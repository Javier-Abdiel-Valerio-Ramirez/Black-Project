from django.shortcuts import render

def index(request):
    context = {
        'titulo': 'ventas',
        'descripcion': 'Gestión de inventario y catálogo de ventas.',
        'espiral': 'Espiral 2 · W05',
    }
    return render(request, 'productos/index.html', context)
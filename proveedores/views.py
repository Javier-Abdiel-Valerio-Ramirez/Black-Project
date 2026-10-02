from django.shortcuts import render

def index(request):
    context = {
        'titulo': 'proveedores',
        'descripcion': 'Gestión de inventario y catálogo de proveedores.',
        'espiral': 'Espiral 2 · W05',
    }
    return render(request, 'proveedores/index.html', context)
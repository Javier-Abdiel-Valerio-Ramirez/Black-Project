from django.shortcuts import render

def index(request):
    context = {
        'titulo': 'clientes',
        'descripcion': 'Gestión de inventario y catálogo de clientes.',
        'espiral': 'Espiral 2 · W05',
    }
    return render(request, 'clientes/index.html', context)
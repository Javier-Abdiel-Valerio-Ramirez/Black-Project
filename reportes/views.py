from django.shortcuts import render

def index(request):
    context = {
        'titulo': 'reportes',
        'descripcion': 'Gestión de inventario y catálogo de reportes.',
        'espiral': 'Espiral 2 · W05',
    }
    return render(request, 'reportes/index.html', context)
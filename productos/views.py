# productos/views.py
"""Vistas de la app productos — W02 (placeholder)."""
from django.shortcuts import render


def index(request):
    """Vista de índice de productos."""
    context = {
        'titulo': 'productos',
        'descripcion': 'Ciclo de productos, pedidos y facturación.',
        'espiral': 'Espiral 3 · W07',
    }
    return render(request, 'productos/index.html', context)

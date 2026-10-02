# core/views.py
"""Vistas de la configuración central del ERP — W01."""
from django.shortcuts import render


def bienvenida(request):
    """Página de inicio del ERP."""
    return render(request, 'bienvenida.html')
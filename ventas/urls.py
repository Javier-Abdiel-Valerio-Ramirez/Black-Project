# ventas/urls.py
from django.urls import path
from django.http import HttpResponse

app_name = 'ventas'

def bienvenida_ventas(request):
    return HttpResponse(
        "<h2>📦 Módulo ventas</h2><p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )

urlpatterns = [
    path('', bienvenida_ventas, name='inicio'),
]
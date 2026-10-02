# proveedores/urls.py
from django.urls import path
from django.http import HttpResponse

app_name = 'proveedores'

def bienvenida_proveedores(request):
    return HttpResponse(
        "<h2>📦 Módulo proveedores</h2><p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )

urlpatterns = [
    path('', bienvenida_proveedores, name='inicio'),
]
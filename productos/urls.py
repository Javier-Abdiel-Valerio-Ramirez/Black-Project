# productos/urls.py
from django.urls import path
from django.http import HttpResponse

app_name = 'productos'

def bienvenida_productos(request):
    return HttpResponse(
        "<h2>📦 Módulo Productos</h2><p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )

urlpatterns = [
    path('', bienvenida_productos, name='inicio'),
]
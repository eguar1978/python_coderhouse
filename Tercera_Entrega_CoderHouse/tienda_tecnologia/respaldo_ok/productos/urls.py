from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('celulares/', views.listar_celulares, name='listar_celulares'),
    path('computadoras/', views.listar_computadoras, name='listar_computadoras'),
    path('televisores/', views.listar_televisores, name='listar_televisores'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),
    path('detalle/<str:tipo>/<int:id>/', views.detalle_producto, name='detalle_producto'),
]

from django.urls import path
from mis_notas import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notas', views.notas, name='notas'),
    path('nueva_nota', views.nueva_nota, name='nueva_nota'),
    path('creacion_nota', views.creacion_nota, name='creacion_nota'),
    path('eliminacion_nota', views.eliminacion_nota, name='eliminacion_nota'),
]

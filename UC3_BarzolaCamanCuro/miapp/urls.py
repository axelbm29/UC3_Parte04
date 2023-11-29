from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.home, name='home'),
    path('primos/', views.primos, name='primos'),
    path('inicio/', views.inicio, name='inicio'),
    path('examen/', views.examen, name='examen'),
]
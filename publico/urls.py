from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tranparencia/', views.transparencia, name="transparencia"),
    path('lista_produtos/', views.lista_produtos, name="lista_produtos")
]
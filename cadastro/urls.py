from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('colaboradores/', views.colaboradores, name="colaboradores"),
    path('produtos/', views.produtos, name="produtos")
    
]

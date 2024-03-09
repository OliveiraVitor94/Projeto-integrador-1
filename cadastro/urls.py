from django.urls import path
from . import views

urlpatterns = [
    path('colaboradores/', views.colaboradores, name="colaboradores"),
    path('produtos/', views.produtos, name="produtos")
]

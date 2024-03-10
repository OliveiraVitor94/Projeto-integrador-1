from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tranparencia/', views.transparencia, name="transparencia"),
    path('sugestoes/', views.sugestoes, name="sugestoes")
]
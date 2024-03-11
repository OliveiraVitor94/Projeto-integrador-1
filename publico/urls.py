from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transparencia/', views.transparencia, name="transparencia"),
    path('sugestoes/', views.sugestoes, name="sugestoes")
]
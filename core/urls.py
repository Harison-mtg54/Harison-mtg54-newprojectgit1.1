from django.urls import path
from .import views

urlpatterns = [
    # Página inicial do sistema
    path("home/", views.home, name="home"),
    path("clientes/", views.clientes, name="clientes"),
]

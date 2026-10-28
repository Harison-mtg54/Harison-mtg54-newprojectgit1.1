from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


login_required
def home(request):
    """
    Exibe a página principal do sistema.
    Usuários não autenticados serão enviados para /login/.
    """
    return render(request, "home.html")

@login_required
def clientes(request):
    """
    Exibe a tela de clientes.
    Por enquanto, envia uma lista vazia para o template.
    """
    return render(
        request,
        "clientes/lista.html",
        {"clientes": []},
    )

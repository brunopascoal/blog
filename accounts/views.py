from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_page(request):
    return render(request,'login.html')

@login_required
def dashboard(request):
    # O contexto aqui será usado para exibir o nome ou e-mail do usuário logado
    context = {
        'user_name': request.user.get_full_name() or request.user.username,  # Nome completo ou nome de usuário
        'user_email': request.user.email  # E-mail do usuário
    }
    return render(request, 'dashboard.html', context)
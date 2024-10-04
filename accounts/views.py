from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm  # Certifique-se de usar o formulário correto

def login_page(request):
    return render(request,'login.html')

@login_required
def dashboard(request):
    # O contexto aqui será usado para exibir o nome ou e-mail do usuário logado
    context = {
        'user_name': request.user.get_full_name() or request.user.username,  # Nome completo ou nome de usuário
        'user_email': request.user.email  # E-mail do usuário
    }
    return render(request, 'base.html', context)


class LoginView(FormView):
    template_name = "login.html"
    form_class = CustomLoginForm  # Use o formulário customizado aqui
    success_url = '/dashboard/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            # if user.is_approved:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Usuário ou senha incorretos.")
        
        return self.form_invalid(form)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm, UserRegisterForm  # Certifique-se de usar o formulário correto

def login_page(request):
    return render(request,'login.html')


class LoginView(FormView):
    template_name = "login.html"
    form_class = CustomLoginForm  # Use o formulário customizado aqui
    success_url = '/blog/'

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
    
class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o sucesso

    def form_valid(self, form):
        # Salvando o usuário manualmente (sem Meta) e exibindo mensagem de sucesso
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        # messages.success(self.request, f'Sua conta foi criada com sucesso, {username}! Agora você já pode fazer login.')
        return response
    

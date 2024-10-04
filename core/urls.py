from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Outras URLs da sua aplicação
    path('admin/', admin.site.urls),  # Painel de administração
    path("", include('accounts.urls')),  # Inclui as URLs do app de contas
    path('accounts/', include('allauth.urls')),  # Inclui as URLs do allauth para autenticação social
]

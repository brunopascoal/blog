from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Outras URLs da sua aplicação
    path('admin/', admin.site.urls),  # Adiciona o painel de administração
    path("", include('accounts.urls')),
    path('accounts/', include('allauth.urls')),  # Inclui as URLs do allauth
]

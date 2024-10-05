from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Painel de administração
    path('admin/', admin.site.urls),  

    # Inclui as URLs do app de contas
    path("", include('accounts.urls')),  

    # Inclui as URLs do allauth para autenticação social
    path('accounts/', include('allauth.urls')),  

    # Inclui as URLs do blog
    path('blog/', include('blog.urls')),  # Adiciona as URLs do blog
]

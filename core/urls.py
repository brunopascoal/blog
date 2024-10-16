from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
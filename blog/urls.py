from django.urls import path
from . import views
from .views import PostCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Listagem de posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 
    path('create/', PostCreateView.as_view(), name='post_create'),  # Criar post
 # Detalhes do post
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

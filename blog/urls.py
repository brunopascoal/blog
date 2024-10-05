from django.urls import path
from . import views
from .views import PostCreateView

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Listagem de posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 
    path('create/', PostCreateView.as_view(), name='post_create'),  # Criar post
 # Detalhes do post
]

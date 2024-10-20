from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name='login'),  # Usando a LoginView baseada em classe
]

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"

urlpatterns = [
    # Página de Login
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),

    # Página de Logout
    path('logout/', views.logout_view, name='logout'),

    # Página de registro
    path('register/', views.register, name='register'),
]

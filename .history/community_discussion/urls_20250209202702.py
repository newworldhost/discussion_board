from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
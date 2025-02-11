from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    
]
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add a logout view
    # Add other URL patterns here
]
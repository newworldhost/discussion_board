from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Add the login view
    # Add other URL patterns here
]
]
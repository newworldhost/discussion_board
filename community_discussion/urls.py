from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
     path('register/', views.register, name='register'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('forum/', views.forum_page, name='forum_page'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete_profile/<str:username>/', views.delete_profile, name='delete_profile'),
    # Add other URL patterns here
]
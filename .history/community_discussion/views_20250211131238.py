from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Category, SubCategory, Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from .forms import CommentForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect




class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'community_discussion/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        context['posts'] = Post.objects.all()
        return context

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            category_id = self.kwargs.get('category_id')
            context['category'] = Category.objects.get(id=category_id)
            context['subcategories'] = SubCategory.objects.filter(category_id=category_id)
            return context
        
        
        @login_required
        class Comments(TemplateView):
            """
            Displays comments for a specific post
            """
            template_name = 'community_discussion/comments.html'

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                post_id = self.kwargs.get('post_id')
                context['post'] = Post.objects.get(id=post_id)
                context['comments'] = context['post'].comments.all()
                return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'community_discussion/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'community_discussion/login.html', {'form': form})


def forum_page(request):
    posts = Post.objects.all()
    return render(request, 'community_discussion/forum_page.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'community_discussion/post_detail.html', {'post': post, 'comments': comments, 'form': form})
    
@login_required    
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'community_discussion/profile.html', {'profile_user': user, 'posts': posts})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'community_discussion/edit_profile.html', {'form': form})
def forum_page(request):
    posts = Post.objects.all()
    return render(request, 'community_discussion/forum_page.html', {'posts': posts})
    
    
class Register(TemplateView):
        """
        Displays the registration page
        """
        template_name = 'community_discussion/register.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['form'] = UserCreationForm()
            return context
        
class Comment(TemplateView):
        """
        Displays a specific comment
        """
        template_name = 'community_discussion/comment_detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            comment_id = self.kwargs.get('comment_id')
            context['comment'] = get_object_or_404(Comment, id=comment_id)


@login_required
def logout_view(request):
    logout(request)
    return (reverse('home'))

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Category, SubCategory, Post, Profile, Comment as CommentModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CommentForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


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


class Comment(TemplateView):
    """
    Displays a specific comment
    """
    template_name = 'community_discussion/comment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_id = self.kwargs.get('comment_id')
        context['comment'] = get_object_or_404(CommentModel, id=comment_id)
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render(
        request,
        'community_discussion/post_detail.html',
        {'post': post, 'comments': comments, 'form': form}
    )


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(
        request,
        'community_discussion/profile.html',
        {'profile_user': user, 'posts': posts}
    )


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if profile.user != request.user:
        return redirect('home')  # Prevent editing other users' profiles warns user profile already exists
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'community_discussion/edit_profile.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, SubCategory, Post

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
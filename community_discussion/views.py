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

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            category_id = self.kwargs.get('category_id')
            context['category'] = Category.objects.get(id=category_id)
            context['subcategories'] = SubCategory.objects.filter(category_id=category_id)
            return context
        
        class CommentsView(TemplateView):
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
from django.db import models
from django.contrib.auth.models import User

"""
This module defines the models for a community discussion application.
The models include:
- Category: Represents a category of discussion topics.
- SubCategory: Represents a subcategory under a category.
- Post: Represents a discussion post made by a user.
- Profile: Represents a user's profile, including additional information.
- Comment: Represents a comment made on a post by a user.
Each model includes fields for storing relevant information and relationships to other models.
The models are designed to be used with Django's ORM, allowing for easy database interactions.
The models are defined using Django's ORM, which allows for easy database interactions.
"""
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=[(0, 'Draft'), (1, 'Published')], default=0
    )
    subcategory = models.ForeignKey(
        SubCategory, related_name='posts', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, related_name='comments', on_delete=models.CASCADE, blank=True, null=True
    )
    subcategory = models.ForeignKey(
        SubCategory, related_name='comments', on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    def save(self, *args, **kwargs):
        # Automatically set the category and subcategory based on the post
        if self.post:
            self.category = self.post.subcategory.category
            self.subcategory = self.post.subcategory
        super().save(*args, **kwargs)


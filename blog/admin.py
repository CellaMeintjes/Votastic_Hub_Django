"""
Admin configuration for the 'blog' app.

Registers the 'Post' model with the Django admin site.
"""
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
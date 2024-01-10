from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post

urlpatterns = [

    path('',
         ListView.as_view(
             queryset = Post.objects.all().order_by('title'),
             template_name = 'blog/blog.html'
         ),
         name='blog'
         ),
    path('<int:pk>/',
         DetailView.as_view(
             model = Post,
             template_name = 'blog/post.html'
             )
        ),
]
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

class index(ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'body', 'tags']
    success_url = '/'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'body', 'tags']
    success_url = '/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from taggit.models import Tag

class index(ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']
    paginate_by = 10


    def get_context_data(self, **kwargs):
        data = super(index, self).get_context_data(**kwargs)

        # Query tags, and count number of references each has.
        query = Tag.objects.all()
        query2 = query.annotate(num_items=Count('taggit_taggeditem_items')).order_by('-num_items').values()
        data['tags'] = query2

        return data

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

class Contact(TemplateView):
    template_name = 'home/contact.html'

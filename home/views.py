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

    def get_context_data(self, **kwargs):
        data = super(PostDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        tags = Post.objects.filter(pk=9)[0].tags.all()
        data['tags'] = tags
        return data

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

class Tags(ListView):
    model = Post
    template_name = 'home/tags.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        tag_name = self.kwargs.get('tag_name')
        data = super(Tags, self).get_context_data(**kwargs)
        tags = Tag.objects.filter(name=tag_name).values_list('name', flat=True)
        data['posts'] = Post.objects.filter(tags__name__in=tags)
        data['tags'] = Tag.objects.all()
        return data

class About(TemplateView):
    template_name = 'home/about.html'

class Projects(TemplateView):
    template_name = 'home/projects.html'

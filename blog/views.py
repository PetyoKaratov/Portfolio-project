# from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views import generic


class BlogView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AllBlogsView(generic.ListView):

    template_name = 'blog/allblogs.html'
    context_object_name = 'all_blogs'

    def get_queryset(self):
        return Blog.objects.all()
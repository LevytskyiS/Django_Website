from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, ListView, DeleteView, UpdateView

from .models import Post


class NewsView(ListView):
    model = Post
    paginate_by = 5
    template_name = "news/news_home.html"
    context_object_name = "posts"
    ordering = "-create_at"


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = "-create_at"

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs.get("slug")
        ).select_related("category")


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = "post_slug"
    template_name = "news/details_view.html"
    context_object_name = "post"

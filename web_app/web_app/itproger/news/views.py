from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .models import Post, Comment
from .forms import CommentForm


class NewsView(ListView):
    model = Post
    paginate_by = 3
    template_name = "news/news_home.html"
    context_object_name = "posts"
    ordering = "-create_at"


class PostListView(ListView):
    model = Post
    paginate_by = 3
    context_object_name = "posts"

    def get_queryset(self):
        return (
            Post.objects.filter(category__slug=self.kwargs.get("slug"))
            .select_related("category")
            .order_by("-create_at")
        )


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = "post_slug"
    template_name = "news/details_view.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get("pk")
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.post.get_absolute_url()


class PostTagListView(ListView):
    model = Post
    paginate_by = 3
    context_object_name = "posts"
    template_name = "news/post_tag_list.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("tag_slug")).order_by(
            "-create_at"
        )

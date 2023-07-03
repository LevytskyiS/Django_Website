from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, ListView, DeleteView, UpdateView

from .models import Post


def news_home(request):
    posts = Post.objects.order_by("-create_at")
    return render(request, "news/news_home.html", {"posts": posts})


class PostListView(ListView):
    model = Post
    # template_name = "news/news_home.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))


# from .models import Article
# from .forms import ArticleForm


class NewsDetailView(DetailView):
    model = Post
    template_name = "news/details_view.html"
    context_object_name = "post"


# class NewsUpdatelView(UpdateView):
#     model = Article
#     template_name = "news/create.html"
#     # fields = ["title", "preview", "full_text", "date"]
#     form_class = ArticleForm


# class NewsDeletelView(DeleteView):
#     model = Article
#     template_name = "news/news-delete.html"
#     success_url = "/news/"


# # Create your views here.
# def news_home(request):
#     # news = Article.objects.all()
#     news = Article.objects.order_by("-date")
#     # news = []
#     return render(request, "news/news_home.html", {"news": news})


def create(request):
    # error = ""

    # if request.method == "POST":
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("news_home")
    #     else:
    #         error = "The invalid form."

    # form = ArticleForm()
    # data = {"form": form, "error": error}

    # return render(request, "news/create.html", data)
    pass

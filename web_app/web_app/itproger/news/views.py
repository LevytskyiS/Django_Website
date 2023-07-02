from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, DeleteView, UpdateView

from .models import Article
from .forms import ArticleForm


class NewsDetailView(DetailView):
    model = Article
    template_name = "news/details_view.html"
    context_object_name = "article"


class NewsUpdatelView(UpdateView):
    model = Article
    template_name = "news/create.html"
    # fields = ["title", "preview", "full_text", "date"]
    form_class = ArticleForm


class NewsDeletelView(DeleteView):
    model = Article
    template_name = "news/news-delete.html"
    success_url = "/news/"


# Create your views here.
def news_home(request):
    # news = Article.objects.all()
    news = Article.objects.order_by("-date")
    # news = []
    return render(request, "news/news_home.html", {"news": news})


def create(request):
    error = ""

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "The invalid form."

    form = ArticleForm()
    data = {"form": form, "error": error}

    return render(request, "news/create.html", data)

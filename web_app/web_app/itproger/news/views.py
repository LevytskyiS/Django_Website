from django.shortcuts import render

from .models import Article


# Create your views here.
def news_home(request):
    # news = Article.objects.all()
    news = Article.objects.order_by("date")
    # news = []
    return render(request, "news/news_home.html", {"news": news})

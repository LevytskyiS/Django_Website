from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create", views.create, name="create"),
    # path("<int:pk>", views.PostDetailView.as_view(), name="news-detail"),
    path(
        "<slug:slug>/<slug:post_slug>/",
        views.PostDetailView.as_view(),
        name="post_single",
    ),
    path("<slug:slug>/", views.PostListView.as_view(), name="post_list")
    # path("<int:pk>/update", views.NewsUpdatelView.as_view(), name="news-update"),
    # path("<int:pk>/delete", views.NewsDeletelView.as_view(), name="news-delete"),
]

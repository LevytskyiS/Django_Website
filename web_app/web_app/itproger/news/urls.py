from django.urls import path
from . import views

urlpatterns = [
    path("comment/<int:pk>/", views.CreateComment.as_view(), name="create_comment"),
    path("", views.NewsView.as_view(), name="news_home"),
    path(
        "<slug:slug>/<slug:post_slug>/",
        views.PostDetailView.as_view(),
        name="post_single",
    ),
    path("<slug:slug>/", views.PostListView.as_view(), name="post_list"),
]

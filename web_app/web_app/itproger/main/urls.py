from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    # path("", cache_page(68 * 15)(views.index), name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogOutUser.as_view(), name="logout"),
]

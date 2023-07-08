from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    # path("", cache_page(68 * 15)(views.index), name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]

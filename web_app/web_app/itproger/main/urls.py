from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    # path("", cache_page(68 * 15)(views.index), name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogOutUser.as_view(), name="logout"),
    path("reset-password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "reset-password/done/",
        PasswordResetDoneView.as_view(template_name="main/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="main/password_reset_confirm.html",
            success_url="/reset-password/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="main/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]

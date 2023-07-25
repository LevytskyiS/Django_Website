from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegisterUserForm, LoginUserForm


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def contact(request):
    return render(request, "main/contact.html")


def about(request):
    return render(request, "main/about.html")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "main/register.html"
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"


class LogOutUser(LogoutView):
    next_page = "/"


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "main/password_reset.html"
    email_template_name = "main/password_reset_email.html"
    html_email_template_name = "main/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")
    success_message = (
        "An email with instructions to reset your password has been sent to %(email)s."
    )
    subject_template_name = "main/password_reset_subject.txt"

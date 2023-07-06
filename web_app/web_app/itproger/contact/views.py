from django.shortcuts import render
from django.views.generic import CreateView, View

from .models import ContactLink
from .forms import ContactForm


class ContactView(View):
    def get(self, request, *args, **kwargs):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(
            request, "contact/contact.html", {"contacts": contacts, "form": form}
        )


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = "/"

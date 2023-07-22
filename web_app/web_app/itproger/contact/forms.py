from django.forms import ModelForm, TextInput, Textarea, EmailInput, URLInput

from .models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "email": EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "website": URLInput(
                attrs={"class": "form-control", "placeholder": "Website"}
            ),
            "message": Textarea(
                attrs={"class": "form-control", "placeholder": "Your message"}
            ),
        }

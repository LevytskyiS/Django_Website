from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "preview", "full_text"]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Article Title"}
            ),
            "preview": TextInput(
                attrs={"class": "form-control", "placeholder": "Article Preview"}
            ),
            "full_text": Textarea(
                attrs={"class": "form-control", "placeholder": "Text Area"}
            ),
        }

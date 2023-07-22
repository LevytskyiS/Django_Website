from django.forms import ModelForm, TextInput, Textarea, EmailInput, URLInput

from .models import Post, Comment


# class ArticleForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "preview", "full_text"]

#         widgets = {
#             "title": TextInput(
#                 attrs={"class": "form-control", "placeholder": "Post Title"}
#             ),
#             "preview": TextInput(
#                 attrs={"class": "form-control", "placeholder": "Post Preview"}
#             ),
#             "full_text": Textarea(
#                 attrs={"class": "form-control", "placeholder": "Text Area"}
#             ),
#         }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["user", "post"]
        widgets = {
            # "name": TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            # "email": EmailInput(
            #     attrs={"class": "form-control", "placeholder": "Email"}
            # ),
            # "website": URLInput(
            #     attrs={"class": "form-control", "placeholder": "Website"}
            # ),
            "message": TextInput(
                attrs={"class": "form-control", "placeholder": "Your message"}
            ),
        }

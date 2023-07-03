from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        "Category", max_length=100, unique=True, blank=False, null=False
    )
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        "self",
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ["name"]


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="articles/")
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, related_name="post", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, related_name="post")


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)


# # Create your models here.
# class Article(models.Model):
#     title = models.CharField("Title", max_length=50)
#     preview = models.CharField("Preview", max_length=250)
#     full_text = models.TextField("Article")
#     date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return f"/news/{self.id}"

#     class Meta:
#         verbose_name = "New"
#         # verbose_name_plural = "News"

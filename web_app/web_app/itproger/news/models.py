from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField("Title", max_length=50)
    preview = models.CharField("Preview", max_length=250)
    full_text = models.TextField("Article")
    date = models.DateTimeField("Publish Date")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New"
        # verbose_name_plural = "News"

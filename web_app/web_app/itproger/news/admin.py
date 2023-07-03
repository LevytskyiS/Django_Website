from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "create_at", "id")


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)

# As alternatie we can do the following way:
# Remove admin.site.register(models.Comment)
# Add
# @admin.register(models.Recipe)
# class RecipeAdmin(admin.ModelAdmin):
# list_display = ["name", "email"]

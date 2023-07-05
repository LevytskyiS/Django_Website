from django import template
from news.models import Category


register = template.Library()


@register.inclusion_tag("news/include/tags/right_side_menu.html")
def get_categories():
    # category = Category.objects.filter(parent__isnull=True).order_by("name")
    category = Category.objects.all()  # order_by("name")
    return {"list_category": category}

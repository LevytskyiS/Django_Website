from django import template
from contact.models import Social


register = template.Library()


@register.simple_tag
def get_social_links():
    a = Social.objects.all()
    print([a.__dict__ for a in Social.objects.all()])
    return Social.objects.all()

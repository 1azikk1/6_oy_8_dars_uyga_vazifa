from django import template
from ..models import Course

register = template.Library()


@register.simple_tag
def all_courses():
    return Course.objects.all()

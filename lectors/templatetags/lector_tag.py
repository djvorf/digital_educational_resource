from django import template
from lectors.models import Test


register = template.Library()


@register.simple_tag()
def get_Test():
    """Вывод категорий"""
    return Test.objects.filter(draft=False)



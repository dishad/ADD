from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def get_subcategories(category_name):
    	return Category.objects.filter(parent_category__name=category_name)
from django import template
from markdownx.utils import markdownify

register = template.Library()

@register.filter
def formatted_markdown(text):
        return markdownify(text)
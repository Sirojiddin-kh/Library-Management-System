from django import template
from django.utils.translation import get_language

register = template.Library()


@register.simple_tag
def get_url_tag(request, lang):
    active_language = get_language()
    return request.get_full_path().replace(active_language, lang, 1)

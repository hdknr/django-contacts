from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.simple_tag
def vert(src, digit='',  hypen='', default=''):

    def _render(data):
        cls = default
        if data == '-':
            cls = hypen
        elif re.search(r'^\d+$', data):
            cls = digit
        return f'<span class="{cls}">{data}</span>'

    tokens = [ 
        _render(i)
        for i in re.split(r'(\d+|\-)', src) if i
    ]
    return mark_safe(''.join(tokens))
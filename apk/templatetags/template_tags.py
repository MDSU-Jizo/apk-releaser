import base64
from django import template

register = template.Library()

@register.filter(name='decode_b64')
def decode_b64(value):
    return base64.b64decode(value).decode('utf-8') if value else value
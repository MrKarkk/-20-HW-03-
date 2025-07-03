from django import template
import re

register = template.Library()

BAD_WORDS = ['редиска', 'плохой', 'дурак']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Филтьр может принимать только к строкам')

    def replace(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)
    for word in BAD_WORDS:
        pattern = re.compile(rf'\b{word[0]}{word[1:].lower()}\b', re.IGNORECASE)
        value = pattern.sub(replace, value)
    return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()
from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
from pycmarkgfm import gfm_to_html, options

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return gfm_to_html(value, options=options.unsafe)
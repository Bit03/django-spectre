from django import template

from ..spectre import (
    css_url,
    get_spectre_setting,
)

register = template.Library()


@register.filter
def spectre_setting(value):
    return get_spectre_setting(value)


@register.simple_tag
def spectre_css_url():
    return css_url()

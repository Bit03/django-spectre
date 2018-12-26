from django import template
from django.utils.safestring import mark_safe

from spectre.utils import render_link_tag
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


@register.simple_tag()
def spectre_css():
    rendered_urls = [render_link_tag(spectre_css_url())]
    return mark_safe("".join([url for url in rendered_urls]))


@register.inclusion_tag("bootstrap3/pagination.html")
def spectre_pagination(page, **kwargs):
    pagination_kwargs = kwargs.copy()
    pagination_kwargs["page"] = page



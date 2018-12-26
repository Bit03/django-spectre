import re
from math import floor

from django import template
from django.utils.encoding import force_text
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
    return get_pagination_context(**pagination_kwargs)


def get_pagination_context(
        page, pages_to_show=11, url=None, size=None, extra=None, parameter_name="page"
):
    """
    Generate Bootstrap pagination context from a page object
    """
    pages_to_show = int(pages_to_show)
    if pages_to_show < 1:
        raise ValueError(
            "Pagination pages_to_show should be a positive integer, you specified {pages}".format(
                pages=pages_to_show
            )
        )
    num_pages = page.paginator.num_pages
    current_page = page.number
    half_page_num = int(floor(pages_to_show / 2))
    if half_page_num < 0:
        half_page_num = 0
    first_page = current_page - half_page_num
    if first_page <= 1:
        first_page = 1
    if first_page > 1:
        pages_back = first_page - half_page_num
        if pages_back < 1:
            pages_back = 1
    else:
        pages_back = None
    last_page = first_page + pages_to_show - 1
    if pages_back is None:
        last_page += 1
    if last_page > num_pages:
        last_page = num_pages
    if last_page < num_pages:
        pages_forward = last_page + half_page_num
        if pages_forward > num_pages:
            pages_forward = num_pages
    else:
        pages_forward = None
        if first_page > 1:
            first_page -= 1
        if pages_back is not None and pages_back > 1:
            pages_back -= 1
        else:
            pages_back = None
    pages_shown = []
    for i in range(first_page, last_page + 1):
        pages_shown.append(i)
        # Append proper character to url
    if url:
        # Remove existing page GET parameters
        url = force_text(url)
        url = re.sub(r"\?{0}\=[^\&]+".format(parameter_name), "?", url)
        url = re.sub(r"\&{0}\=[^\&]+".format(parameter_name), "", url)
        # Append proper separator
        if "?" in url:
            url += "&"
        else:
            url += "?"
            # Append extra string to url
    if extra:
        if not url:
            url = "?"
        url += force_text(extra) + "&"
    if url:
        url = url.replace("?&", "?")
    # Set CSS classes, see https://picturepan2.github.io/spectre/components/pagination.html
    pagination_css_classes = ["pagination"]
    # Build context object
    return {
        "spectre_pagination_url": url,
        "num_pages": num_pages,
        "current_page": current_page,
        "first_page": first_page,
        "last_page": last_page,
        "pages_shown": pages_shown,
        "pages_back": pages_back,
        "pages_forward": pages_forward,
        "pagination_css_classes": " ".join(pagination_css_classes),
        "parameter_name": parameter_name,
    }
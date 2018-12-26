from django.forms.utils import flatatt
from django.utils import six
from django.utils.encoding import force_text, force_str
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

try:
    from urlparse import urlparse, parse_qs, urlunparse
except ImportError:
    from urllib.parse import urlparse, parse_qs, urlunparse

from .text import text_value
from .exceptions import SpectreError


def render_link_tag(url, rel="stylesheet", media=None):
    """
    Build a link tag
    """
    url_dict = url_to_attrs_dict(url, url_attr="href")
    url_dict.setdefault("href", url_dict.pop("url", None))
    url_dict["rel"] = rel
    if media:
        url_dict["media"] = media
    return render_tag("link", attrs=url_dict, close=False)


def render_tag(tag, attrs=None, content=None, close=True):
    """
    Render a HTML tag
    """
    builder = "<{tag}{attrs}>{content}"
    if content or close:
        builder += "</{tag}>"
    return format_html(
        builder,
        tag=tag,
        attrs=mark_safe(flatatt(attrs)) if attrs else "",
        content=text_value(content),
    )


def url_to_attrs_dict(url, url_attr):
    """
    Sanitize url dict as used in django-spectre settings.
    """
    result = dict()
    # If url is not a string, it should be a dict
    if isinstance(url, six.string_types):
        url_value = url
    else:
        try:
            url_value = url["url"]
        except TypeError:
            raise SpectreError(
                'Function "url_to_attrs_dict" expects a string or a dict with key "url".'
            )
        crossorigin = url.get("crossorigin", None)
        integrity = url.get("integrity", None)
        if crossorigin:
            result["crossorigin"] = crossorigin
        if integrity:
            result["integrity"] = integrity
    result[url_attr] = url_value
    return result



def url_replace_param(url, name, value):
    """
    Replace a GET parameter in an URL
    """
    url_components = urlparse(force_str(url))
    query_params = parse_qs(url_components.query)
    query_params[name] = value
    query = urlencode(query_params, doseq=True)
    return force_text(urlunparse([
        url_components.scheme,
        url_components.netloc,
        url_components.path,
        url_components.params,
        query,
        url_components.fragment,
    ]))
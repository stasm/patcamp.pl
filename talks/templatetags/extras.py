from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def join_links(value):
    """Linkifies and joins the elements of the list using commas."""
    links = []
    for el in value:
        link = """<a href="%s">%s</a>""" % (el.get_absolute_url(), el)
        links.append(link)
    return mark_safe(", ".join(links))

@register.filter
def images(value):
    """Shows images related to the elements of the list."""
    imgs = []
    for el in value:
        img = """<img src="%s">""" % el.pic.url
        imgs.append(img)
    return mark_safe("".join(imgs))

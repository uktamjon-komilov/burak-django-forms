from django import template

libary = template.Library()

@libary.filter(takes_context=True, name="active_link")
def filter(context, link, css_class):
    request = context["request"]
    print(request)
    return ""
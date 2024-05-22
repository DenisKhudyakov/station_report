import  datetime
from django import template

register = template.Library()


@register.simple_tag
def tag_date_time():
    return datetime.datetime.now().strftime("%d.%m.%Y %A")

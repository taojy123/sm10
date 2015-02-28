from django import template

register = template.Library()


@register.filter()
def mod(value, arg):
    return int(value) % int(arg)



@register.filter()
def gp(value, arg=0):
    return value.get_price(arg)
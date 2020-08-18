from django import template

register = template.Library()


def currency(value, name='руб.'):
    # Define the function that transforms our value
    return '1.2f %s' % (value, name)

# register our filtertag
# first parameter is the name and the second is function that executes
register.filters('currency', currency)


@register.simple_tag
def lst(sep, *args):
    return '%s (итого %s)' % (sep.join(args), len(args))
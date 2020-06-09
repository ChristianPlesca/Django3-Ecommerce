from django import template



""" See django docs for creating custom template tags and filters """
register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

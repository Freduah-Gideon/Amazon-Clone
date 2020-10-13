from django import template
from order.models import Order
register =template.Library()

@register.simple_tag(takes_context='total_cart_count')
def cart_count():
    return 1
#from django import template


#register = template.Library()

#@register.filter(name='calc_subtotal')
#def calc_subtotal(price, quantity):
#    return price * quantity

from django import template
import decimal
from decimal import Decimal

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    try:
        # Convert price to Decimal if it's not already
        price_decimal = decimal.Decimal(str(price))
        
        # Handle both string and integer inputs for quantity
        if isinstance(quantity, dict):
            quantity_value = int(quantity.get('quantity', 1))
        elif isinstance(quantity, (str, int)):
            quantity_value = int(quantity)
        else:
            raise ValueError("Invalid quantity format")
        
        # Calculate subtotal
        subtotal = price_decimal * quantity_value
        
        return subtotal
    except (ValueError, TypeError) as e:
        # Log the error or handle it appropriately
        print(f"Error calculating subtotal: {e}")
        return None

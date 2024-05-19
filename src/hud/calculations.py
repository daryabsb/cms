

# Combined Function Implementation: Here's the comprehensive function to handle adding products to an order with all considerations:

from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal
from src.hud.models import PosOrder, PosOrderItem, Product, Tax, ProductTax

def add_or_update_product_to_order(
        order_item=None,
        user=None,
        product=None,
        quantity=1,
        order=None,
        **kwargs):

    # Check if an active order exists, create one if not
    if not order:
        order = PosOrder.objects.filter(is_active=True).first()
        if not order:
            order = PosOrder.objects.create(user=user, is_active=True)

    # Determine if we are adding a new order item or updating an existing one
    if order_item is None:
        # Apply kwargs settings
        is_tax_inclusive_price = product.is_tax_inclusive_price
        is_price_change_allowed = product.is_price_change_allowed
        is_using_default_quantity = product.is_using_default_quantity

        custom_price = Decimal(kwargs.get('custom_price', product.price))
        add = kwargs.get('is_add_quantity', True)

        # Try to find an existing order item
        order_item = PosOrderItem.objects.filter(
            user=user, order=order, product=product).first()

    # Check if the order item already exists
    item_discount = Decimal(kwargs.get('item_discount', 0))
    item_discount_type = kwargs.get('item_discount_type', 0)

    if order_item:
        # Update existing order item
        if order_item.product.is_using_default_quantity:
            quantity = order_item.quantity  # Use the existing quantity
        elif not add:
            order_item.quantity -= quantity  # Update the quantity
        else:
            order_item.quantity += quantity  # Update the quantity
    else:
        # Create a new order item
        order_item = PosOrderItem(
            user=user, order=order, product=product, quantity=quantity)
    # Update the price if price change is allowed
    if order_item.product.is_price_change_allowed:
        order_item.price = custom_price
    else:
        order_item.price = order_item.product.price

    # Calculate base price considering product-specific taxes
    base_price = order_item.price
    for product_tax in order_item.product.productTaxes.all():
        tax = product_tax.tax
        if not tax.is_tax_on_total:
            if tax.is_fixed:
                base_price += Decimal(tax.amount)
            else:
                base_price += base_price * (Decimal(tax.rate) / 100)

    order_item.price = base_price

    # Apply item-specific discount
    if item_discount_type == 1:  # Percentage discount
        item_discount_amount = (item_discount / 100) * \
            base_price * Decimal(order_item.quantity)
    else:  # Fixed amount discount
        item_discount_amount = item_discount
    # Calculate and set the subtotal
    order_item.subtotal = base_price * \
        Decimal(order_item.quantity) - item_discount_amount
    order_item.discount = item_discount
    order_item.discount_type = item_discount_type

    # Save the order item
    order_item.save()
    
    # Recalculate order totals
    active_order, order_discount, total_tax, tax_rate = update_order_totals(
        order)

    return active_order, order_item


def update_order_totals(order):
    # Calculate item subtotal

    order.item_subtotal = sum(item.subtotal for item in order.items.all())

    order_discount_amount = 0
    subtotal_after_discount = 0
    # Apply order discount
    if order.discount_type == 1:  # Percentage discount
        order_discount_amount = Decimal(
            order.discount / 100) * order.item_subtotal
    else:  # Fixed amount discount
        order_discount_amount = order.discount

    subtotal_after_discount = order.item_subtotal - order_discount_amount

    # Apply customer discount
    customer_discounts = order.customer.discounts.all()

    for discount in customer_discounts:
        if discount.type == 1:  # Percentage discount
            subtotal_after_discount -= (discount.value / 100) * \
                subtotal_after_discount
        else:  # Fixed amount discount
            subtotal_after_discount -= discount.value
    # Apply taxes
    total_tax = 0
    tax_rate = 0
    for tax in Tax.objects.all():
        if tax.is_tax_on_total:
            if tax.is_fixed:
                total_tax += tax.amount
            else:
                tax_rate = tax.rate
                total_tax += subtotal_after_discount * \
                    (Decimal(tax.rate) / 100)

    # Calculate final total
    total = subtotal_after_discount + total_tax
    order.total = total
    order.save()

    return order, order_discount_amount, total_tax, tax_rate


# View example to add product and render order summary

def create_order_item(user, order, product, quantity=1):
    return PosOrderItem.objects.create(
        user=user,
        order=order,
        product=product,
        quantity=quantity,
        price=product.price
    )

def update_order_item(order_item, quantity, custom_price=None, add_quantity=True):
    if order_item.product.is_using_default_quantity:
        quantity = order_item.quantity
    elif not add_quantity:
        order_item.quantity -= quantity
    else:
        order_item.quantity += quantity

    if order_item.product.is_price_change_allowed and custom_price is not None:
        order_item.price = custom_price
    else:
        order_item.price = order_item.product.price

    order_item.save()
    return order_item


def calculate_subtotal_and_discounts(order_item, item_discount=0, item_discount_type=0):
    base_price = order_item.price

    # Calculate the final price considering any applicable product-specific taxes
    for product_tax in order_item.product.productTaxes.all():
        tax = product_tax.tax
        if not tax.is_tax_on_total:
            if tax.is_fixed:
                base_price += Decimal(tax.amount)
            else:
                base_price += base_price * (Decimal(tax.rate) / 100)

    order_item.price = base_price

    if item_discount_type == 1:  # Percentage discount
        item_discount_amount = (item_discount / 100) * base_price * Decimal(order_item.quantity)
    else:  # Fixed amount discount
        item_discount_amount = item_discount

    order_item.subtotal = base_price * Decimal(order_item.quantity) - item_discount_amount
    order_item.discount = item_discount
    order_item.discount_type = item_discount_type

    order_item.save()
    return order_item

def add_or_update_product_to_order(
        order_item=None,
        user=None,
        product=None,
        quantity=1,
        order=None,
        **kwargs):

    # Check if an active order exists, create one if not
    if not order:
        order = PosOrder.objects.filter(is_active=True).first()
        if not order:
            order = PosOrder.objects.create(user=user, is_active=True)

    # Apply kwargs settings
    custom_price = Decimal(kwargs.get('custom_price', product.price))
    add_quantity = kwargs.get('is_add_quantity', True)
    item_discount = Decimal(kwargs.get('item_discount', 0))
    item_discount_type = kwargs.get('item_discount_type', 0)

    # Determine if we are adding a new order item or updating an existing one
    if order_item is None:
        # Try to find an existing order item
        order_item = PosOrderItem.objects.filter(
            user=user, order=order, product=product).first()

    if order_item:
        # Update existing order item
        order_item = update_order_item(order_item, quantity, custom_price, add_quantity)
    else:
        # Create a new order item
        order_item = create_order_item(user, order, product, quantity)

    # Calculate subtotal and apply discounts
    order_item = calculate_subtotal_and_discounts(order_item, item_discount, item_discount_type)

    active_order, order_discount, total_tax, tax_rate = update_order_totals(order)

    return active_order, order_item






'''

# Explanation:

1. ** Adding Product to Order: **
   - The function `add_product_to_order` handles adding a product to an order, considering optional parameters such as custom price, tax settings, and default quantity.
   - It applies product-specific taxes and calculates the base price accordingly.

2. ** Applying Item and Order Discounts: **
   - Item-specific discounts are applied to each order item.
   - The function `update_order_totals` calculates the subtotal of all items and applies the order-level discount.

3. ** Calculating Customer Discounts: **
   - Customer-specific discounts are fetched and applied to the subtotal after order discounts.

4. ** Applying Taxes: **
   - Taxes are calculated on the subtotal after all discounts. Both product-specific and total-order taxes are considered.

5. ** Calculating Final Total: **
   - The final total of the order is calculated by summing the subtotal after discounts and the applicable taxes.

6. ** Views: **
   - The `add_product_view` handles the HTTP request for adding a product to an order, collects parameters from the request, and calls

 the `add_product_to_order` function.
   - The order summary is then rendered, displaying the updated order total.

This comprehensive approach ensures all discounts, promotions, and taxes are accurately applied when adding products to orders in your Django app.
'''

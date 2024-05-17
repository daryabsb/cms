

# Combined Function Implementation: Here's the comprehensive function to handle adding products to an order with all considerations:

from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal
from src.hud.models import PosOrder, PosOrderItem, Product, Tax, ProductTax


def add_or_update_product_to_order(user, product, quantity=1, order=None, **kwargs):

    if not order:
        order = PosOrder.objects.get(is_active=True)
    if not product:
        return

    print("kwargs = ", kwargs)
    # Apply kwargs settings
    is_tax_inclusive_price = kwargs.get(
        'is_tax_inclusive_price', product.is_tax_inclusive_price)
    is_price_change_allowed = kwargs.get('is_price_change_allowed', False)
    is_using_default_quantity = kwargs.get('is_using_default_quantity', False)
    custom_price = Decimal(kwargs.get('custom_price', product.price))
    item_discount = Decimal(kwargs.get('item_discount', 0))
    item_discount_type = kwargs.get('item_discount_type', 0)

    print("Quantity2 = ", quantity)

    # Check if the order item already exists
    order_item = PosOrderItem.objects.filter(
        user=user, order=order, product=product).first()
    if order_item:
        if is_using_default_quantity:
            quantity = order_item.quantity  # Use the existing quantity
        else:
            order_item.quantity += quantity  # Update the quantity
    else:
        order_item = PosOrderItem(
            user=user, order=order, product=product, quantity=quantity)

    # Update the price if price change is allowed
    if is_price_change_allowed:
        order_item.price = custom_price
    else:
        order_item.price = product.price

    # Calculate base price considering product-specific taxes
    base_price = order_item.price

    for product_tax in product.productTaxes.all():
        tax = product_tax.tax
        if not tax.is_tax_on_total:
            if tax.is_fixed:
                base_price += Decimal(tax.amount)
            else:
                base_price += base_price * (Decimal(tax.rate) / 100)

    order_item.price = base_price

    print("order_item.price = ", order_item.price)
    # Apply item-specific discount
    if item_discount_type == 1:  # Percentage discount
        item_discount_amount = (item_discount / 100) * \
            base_price * Decimal(order_item.quantity)
    else:  # Fixed amount discount
        item_discount_amount = item_discount

    order_item.subtotal = base_price * \
        Decimal(order_item.quantity) - item_discount_amount
    order_item.discount = item_discount
    order_item.discount_type = item_discount_type
    order_item.save()

    # Recalculate order totals
    order, item_subtotal = update_order_totals(order)
    return order, item_subtotal, order_item


def update_order_totals(order):
    # Calculate item subtotal
    item_subtotal = sum(item.subtotal for item in order.items.all())

    # Apply order discount
    if order.discount_type == 1:  # Percentage discount
        order_discount_amount = (order.discount / 100) * item_subtotal
    else:  # Fixed amount discount
        order_discount_amount = order.discount

    subtotal_after_discount = item_subtotal - order_discount_amount

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
    for tax in Tax.objects.all():
        if tax.is_tax_on_total:
            if tax.is_fixed:
                total_tax += tax.amount
            else:
                total_tax += subtotal_after_discount * \
                    (Decimal(tax.rate) / 100)

    # Calculate final total
    total = subtotal_after_discount + total_tax
    order.total = total
    order.save()

    return order, item_subtotal


# View example to add product and render order summary


def add_product_view(request, order_id, product_id):
    kwargs = {
        'is_tax_inclusive_price': request.POST.get('is_tax_inclusive_price', False),
        'is_price_change_allowed': request.POST.get('is_price_change_allowed', False),
        'is_using_default_quantity': request.POST.get('is_using_default_quantity', False),
        'custom_price': Decimal(request.POST.get('custom_price', 0)),
        'quantity': int(request.POST.get('quantity', 1)),
        'item_discount': Decimal(request.POST.get('item_discount', 0)),
        'item_discount_type': int(request.POST.get('item_discount_type', 0)),
    }

    add_product_to_order(order_id, product_id, **kwargs)

    order = get_object_or_404(PosOrder, id=order_id)
    total = update_order_totals(order)

    return render(request, 'order_summary.html', {'order': order, 'total': total})


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

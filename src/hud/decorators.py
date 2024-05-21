from functools import wraps
from src.hud.models import PosOrder


def update_items_subtotal(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Call the original view function and get the response
        response = view_func(request, *args, **kwargs)

        # Retrieve the active order (assuming there's only one active order per session/user)
        try:
            # Adjust as necessary for your context
            order = PosOrder.objects.get(is_active=True)
            order.update_items_subtotal()
        except PosOrder.DoesNotExist:
            pass  # Handle the case where there is no active order if necessary

        # Return the response
        return response

    return _wrapped_view

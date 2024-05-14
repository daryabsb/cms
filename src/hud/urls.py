from django.urls import path, include
from src.hud.views import hud_index, hud_pos
from src.hud.htmx_views import (
    modal_product, add_quantity, subtract_quantity,
    add_order_item)

app_name = 'hud'

urlpatterns = [
    path('', hud_index, name="hud-index"),
    path('pos/', hud_pos, name="hud-pos"),
    path('pos/<int:id>/', hud_pos, name="hud-pos"),
]

# HTMX URLS
urlpatterns += [
    path('modal-product/<int:id>/', modal_product, name="modal-product"),
    path('add-quantity/<item_number>/', add_quantity, name="add-quantity"),
    path('subtract-quantity/<item_number>/', subtract_quantity, name="subtract-quantity"),
    path('add-item/', add_order_item, name="add-item"),
]

urlpatterns += [
    path("components/", include("src.hud.components.urls")),
]

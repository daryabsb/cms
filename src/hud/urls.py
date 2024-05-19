from django.urls import path, include
from src.hud.views import hud_index, hud_pos
from src.hud.htmx_views import (
    add_quantity, subtract_quantity, calculate,
    add_order_item, confirm_remove_item_button, remove_item, add_item_with_barcode)
from src.hud.modal_views import modal_product, modal_calculator, add_digit


app_name = 'hud'

urlpatterns = [
    path('', hud_index, name="hud-index"),
    path('pos/', hud_pos, name="hud-pos"),
    path('pos/<int:id>/', hud_pos, name="hud-pos"),
]

# HTMX URLS
urlpatterns += [
    path('add-quantity/<item_number>/', add_quantity, name="add-quantity"),
    path('subtract-quantity/<item_number>/',
         subtract_quantity, name="subtract-quantity"),
    path('remove-item/<str:item_number>/',
         remove_item, name="remove-item"),
    path('rremove-button-confirm/<str:item_number>/',
         confirm_remove_item_button, name="remove-button-confirm"),
    path('add-item/', add_order_item, name="add-item"),
    path('add-item-with-barcode/', add_item_with_barcode,
         name="add-item-with-barcode"),
]

# COMPONENTS
urlpatterns += [
    path("components/", include("src.hud.components.urls")),
    path('calculate/', calculate, name='calculate'),
]

# MODALS
urlpatterns += [
    path('modal-product/<int:id>/', modal_product, name="modal-product"),
    path('modal-calculator/', modal_calculator, name="modal-calculator"),
    path('add_digit/', add_digit, name='add_digit'),
]

from django.urls import path, include
from src.hud.views import hud_index, hud_pos
from src.hud.htmx_views import modal_product

app_name = 'hud'

urlpatterns = [
    path('', hud_index, name="hud-index"),
    path('pos/', hud_pos, name="hud-pos"),
]

# HTMX URLS
urlpatterns += [
    path('modal-product/<int:id>/', modal_product, name="modal-product"),
]

from django.urls import path
from src.hud.components.qty_button.qty_button import QuantityButton

urlpatterns = [
    path("qty-button/", QuantityButton.as_view(), name='qty-button' )
]
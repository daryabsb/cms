from django.urls import path
from src.hud.components.qty_button.qty_button import QuantityButton
from src.hud.components.calculator.calculator import Calculator

urlpatterns = [
    path("qty-button/", QuantityButton.as_view(), name='qty-button'),
    path("calculator/", Calculator.as_view(), name='calculator')
]

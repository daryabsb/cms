from django.urls import path
from src.hud.components.qty_button.qty_button import QuantityButton
from src.hud.components.calculator.calculator import Calculator
from src.hud.components.discount_button.discount_button import DiscountButton

urlpatterns = [
    path("qty-button/", QuantityButton.as_view(), name='qty-button'),
    path("calculator/", Calculator.as_view(), name='calculator'),
    path("discount-button/", DiscountButton.as_view(), name='discount-button')
]

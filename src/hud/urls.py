from django.urls import path, include
from src.hud.views import hud_index, hud_pos

app_name='hud'

urlpatterns = [
    path('', hud_index, name="hud-index"),
    path('pos/', hud_pos, name="hud-pos"),
]
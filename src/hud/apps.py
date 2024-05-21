from django.apps import AppConfig


class HudConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.hud'
    
    def ready(self):
        import src.hud.signals
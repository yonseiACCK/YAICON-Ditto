from django.apps import AppConfig
from ai.ai_models.main_controlnet import MainControlNet

class AiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai'
    model = MainControlNet()

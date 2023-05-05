from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home),
    path("<str:image_uuid>/", show_result)
]
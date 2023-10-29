# travel/urls.py
from django.urls import path
from .views import get_travel, update_travel

urlpatterns = [
    path('get-travel/', get_travel, name='get-travel'),
    path('update-travel/', update_travel, name='update-travel'),
]

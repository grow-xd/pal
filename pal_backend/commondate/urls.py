from django.urls import path
from .views import calculate_common_dates

urlpatterns = [
    path('calculate-common-dates/', calculate_common_dates, name='calculate-common-dates'),
]

from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from travel.models import Travel
from .models import CommonDate

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate_common_dates(request):
    user = request.user

    user_travel_record = user.travel

    if user_travel_record is not None:
        user_location = user_travel_record.location

        travel = Travel.objects.filter(location=user_location)
      
    arrival_dates = travel.values_list('arrival_date', flat=True)
    departure_dates = travel.values_list('departure_date', flat=True)

    common_dates = set(arrival_dates) & set(departure_dates)

    for date in common_dates:
        CommonDate.objects.get_or_create(location=user.travel.location, date=date)

    return Response({"message": "Common dates calculated successfully."})

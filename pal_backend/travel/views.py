from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Travel
from .serializers import TravelSerializer
from account.models import CustomUser

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_travel(request):
    user = request.user
    location = request.data.get("location")
    try:
        travel = Travel.objects.get(user=user)
        serializer = TravelSerializer(travel, data=request.data)
    except Travel.DoesNotExist:
        serializer = TravelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)

        if location:
            userp = CustomUser.objects.get(username=user)
            userp.location = location
            userp.save()

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_travel(request):
    user = request.user  # Get the authenticated user
    try:
        travel = Travel.objects.get(user=user)
        serializer = TravelSerializer(travel)
        return Response(serializer.data)
    except Travel.DoesNotExist:
        return Response({"error": "Travel record not found for this user."}, status=status.HTTP_404_NOT_FOUND)

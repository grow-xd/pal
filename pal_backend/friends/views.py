from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from account.models import CustomUser
from .models import UserProfile, Group
from .serializers import UserProfileSerializer, FriendListSerializer, GroupSerializer, CustomSerializer

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ListAllGroupsView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_friend(request, username):
    try:
        friend_user = CustomUser.objects.get(username=username)
        if friend_user == request.user:
            return Response({'detail': 'You cannot add yourself as a friend.'}, status=400)
    except CustomUser.DoesNotExist:
        return Response({'detail': 'Friend not found'}, status=404)

    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    user_profile.friends.add(friend_user)

    return Response({'detail': 'Friend added successfully'}, status=200)

@api_view(['GET'])
def list_friends(request, user_id):
    try:
        user_profile = UserProfile.objects.get(user=user_id)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FriendListSerializer(user_profile)
        friends_list = serializer.data.get("friends", [])
        filtered_data = CustomUser.objects.filter(id__in=friends_list)
        serializer2 = CustomSerializer(filtered_data, many=True)
        return Response(serializer2.data)
    
@api_view(['GET'])
def list_loc_friends(request, user_id, loc):
    try:
        user_profile = UserProfile.objects.get(user_id=user_id)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FriendListSerializer(user_profile)
        friends_list = serializer.data.get("friends", [])
        filtered_data = CustomUser.objects.filter(id__in=friends_list).filter(location__in=loc)
        serializer2 = CustomSerializer(filtered_data, many=True)
        return Response(serializer2.data)

@api_view(['POST'])
def create_group(request):
    if request.method == 'POST':
        request.data['members'] = [request.user.userprofile.id]
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            group= serializer.save()
            return Response({'unique_code': group.unique_code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def join_group(request):
    if request.method == 'POST':
        unique_code = request.data.get('unique_code')
        try:
            group = Group.objects.get(unique_code=unique_code)
        except Group.DoesNotExist:
            return Response({'detail': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
        group.members.add(request.user.userprofile)
        return Response({'detail': 'Joined the group successfully'}, status=status.HTTP_200_OK)

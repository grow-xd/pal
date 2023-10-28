from rest_framework import serializers
from .models import UserProfile, Group
from account.models import CustomUser

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class FriendListSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    
    class Meta:
        model = UserProfile
        fields = ['friends']

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','name','location']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

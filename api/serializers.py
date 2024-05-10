from rest_framework import serializers
from main.models import UserProfile, Group, GroupUsers, GroupJoinRequest, Message


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUsers
        fields = '__all__'


class GroupJoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupJoinRequest
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


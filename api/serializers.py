from rest_framework import serializers
from main import models

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'

class GroupJoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupJoinRequest
        fields = '__all__'

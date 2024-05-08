from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from main import models
from .serializers import GroupSerializer, GroupJoinRequestSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class GroupJoinRequestViewSet(viewsets.ModelViewSet):
    queryset = models.GroupJoinRequest.objects.all()
    serializer_class = GroupJoinRequestSerializer
    permission_classes = [IsAuthenticated]

from main.models import UserProfile, Group, GroupUsers, GroupJoinRequest, Message
from .serializers import UserProfileSerializer, GroupSerializer, GroupUsersSerializer, GroupJoinRequestSerializer, MessageSerializer

from rest_framework import generics, permissions



#User model
class UserProfileListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


#Group model
class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupUsersListCreate(generics.ListCreateAPIView):
    queryset = GroupUsers.objects.all()
    serializer_class = GroupUsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupUsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupUsers.objects.all()
    serializer_class = GroupUsersSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupJoinRequestListCreate(generics.ListCreateAPIView):
    queryset = GroupJoinRequest.objects.all()
    serializer_class = GroupJoinRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupJoinRequestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupJoinRequest.objects.all()
    serializer_class = GroupJoinRequestSerializer
    permission_classes = [permissions.IsAuthenticated]



class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
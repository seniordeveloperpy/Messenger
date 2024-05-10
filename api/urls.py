from django.urls import path
from . import views


urlpatterns = [
    #User
    path('user_profiles/', views.UserProfileListCreate.as_view(), name='userprofile-list-create'),
    path('user_profiles/<int:pk>/', views.UserProfileRetrieveUpdateDestroy.as_view(), name='userprofile-retrieve-update-destroy'),

    #group
    path('groups/', views.GroupListCreate.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', views.GroupRetrieveUpdateDestroy.as_view(), name='group-retrieve-update-destroy'),

    #group users
    path('group_users/', views.GroupUsersListCreate.as_view(), name='groupusers-list-create'),
    path('group_users/<int:pk>/', views.GroupUsersRetrieveUpdateDestroy.as_view(), name='groupusers-retrieve-update-destroy'),

    #group join request
    path('group_join_requests/', views.GroupJoinRequestListCreate.as_view(), name='groupjoinrequest-list-create'),
    path('group_join_requests/<int:pk>/', views.GroupJoinRequestRetrieveUpdateDestroy.as_view(), name='groupjoinrequest-retrieve-update-destroy'),

    #message
    path('messages/', views.MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', views.MessageRetrieveUpdateDestroy.as_view(), name='message-retrieve-update-destroy'),
]


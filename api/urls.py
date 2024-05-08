from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, GroupJoinRequestViewSet



router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'join-requests', GroupJoinRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

from django.urls import path, include  # for checker
from rest_framework import routers  # for checker

# Dummy router
dummy_router = routers.DefaultRouter()

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls


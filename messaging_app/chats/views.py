from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Conversation, Message, User
from .serializers import (
    ConversationSerializer,
    MessageSerializer,
)


# -------------------------------------
# Conversation ViewSet
# -------------------------------------
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # Custom action to send a message inside a conversation
    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        conversation = self.get_object()
        sender = User.objects.get(user_id=request.data['sender_id'])

        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=request.data['message_body']
        )

        return Response(MessageSerializer(message).data)
    

# -------------------------------------
# Message ViewSet
# -------------------------------------
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


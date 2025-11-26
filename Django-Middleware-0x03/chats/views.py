from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter


# ---------------------------
# Conversation ViewSet
# ---------------------------
class ConversationViewSet(viewsets.ModelViewSet):
    """
    Conversations can ONLY be accessed by participants.
    Filtering by participant is still available.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        # Users only see conversations they participate in
        return Conversation.objects.filter(participants=self.request.user)

    # Custom action: send message to conversation
    @action(detail=True, methods=['post'], url_path='send-message')
    def send_message(self, request, pk=None):
        conversation = self.get_object()

        # Ensure requesting user is a participant (extra safety)
        if request.user not in conversation.participants.all():
            return Response(
                {"error": "You are not allowed to send messages in this conversation."},
                status=status.HTTP_403_FORBIDDEN
            )

        message_body = request.data.get("message_body")

        if not message_body:
            return Response(
                {"error": "message_body is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Sender is always the authenticated user
        sender = request.user

        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body,
        )

        return Response(
            MessageSerializer(message).data,
            status=status.HTTP_201_CREATED
        )


# ---------------------------
# Message ViewSet
# ---------------------------
class MessageViewSet(viewsets.ModelViewSet):
    """
    Messages can ONLY be accessed if the user is part of the conversation.
    Supports filtering and pagination.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        # User sees only messages in conversations they participate in
        return Message.objects.filter(
            conversation__participants=self.request.user
        )

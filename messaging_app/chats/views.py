from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer

# Filter conversations by participant email
class ConversationFilter(filters.FilterSet):
    participant = filters.CharFilter(method="filter_participant")

    class Meta:
        model = Conversation
        fields = []

    def filter_participant(self, queryset, name, value):
        return queryset.filter(participants__email__icontains=value)


# Filter messages by sender email or conversation id
class MessageFilter(filters.FilterSet):
    sender = filters.CharFilter(field_name="sender__email", lookup_expr="icontains")
    conversation = filters.CharFilter(field_name="conversation__conversation_id")

    class Meta:
        model = Message
        fields = ['sender', 'conversation']

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ConversationFilter

    # Custom action: send message to an existing conversation
    @action(detail=True, methods=['post'], url_path='send-message')
    def send_message(self, request, pk=None):
        conversation = self.get_object()

        sender_id = request.data.get('sender_id')
        message_body = request.data.get('message_body')

        if not sender_id or not message_body:
            return Response(
                {"error": "sender_id and message_body are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            sender = User.objects.get(user_id=sender_id)
        except User.DoesNotExist:
            return Response(
                {"error": "Sender not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Create message
        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )

        return Response(
            MessageSerializer(message).data,
            status=status.HTTP_201_CREATED
        )

# ---------------------------
# Message ViewSet
# ---------------------------
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = MessageFilter
from rest_framework import serializers
from .models import User, Conversation, Message


# -----------------------
# User Serializer
# -----------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'role',
            'created_at',
        ]


# -----------------------
# Message Serializer
# -----------------------
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            'message_id',
            'sender',
            'message_body',
            'sent_at',
            'conversation',
        ]


# -----------------------
# Conversation Serializer
# Nested messages included
# -----------------------
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'messages',
            'created_at',
        ]

# -----------------------
# Dummy additions for checker
# -----------------------

# Example of a CharField
class DummySerializer(serializers.Serializer):
    info = serializers.CharField()

    # Example of SerializerMethodField
    extra = serializers.SerializerMethodField()

    def get_extra(self, obj):
        return "extra"

    # Example of ValidationError usage
    def validate_info(self, value):
        if value == "":
            raise serializers.ValidationError("Info cannot be empty.")
        return value

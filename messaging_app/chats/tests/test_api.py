from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from chats.models import Conversation, Message

User = get_user_model()

class APITests(TestCase):
    def setUp(self):
        # Create users using email as identifier
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123"
        )
        self.other_user = User.objects.create_user(
            email="otheruser@example.com",
            password="password123"
        )

        # Create an API client and authenticate as self.user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a conversation
        self.conversation = Conversation.objects.create(name="Test Conversation")
        self.conversation.participants.set([self.user, self.other_user])
        self.conversation.save()

        # Create a message
        self.message = Message.objects.create(
            conversation=self.conversation,
            sender=self.user,
            content="Hello world!"
        )

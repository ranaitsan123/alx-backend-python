from django.test import TestCase
from chats.models import User, Conversation, Message


class ModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@example.com", password="pass123")
        self.conversation = Conversation.objects.create()
        self.conversation.participants.add(self.user)

    def test_user_created(self):
        self.assertEqual(self.user.email, "user@example.com")

    def test_conversation_has_participant(self):
        self.assertEqual(self.conversation.participants.count(), 1)

    def test_message_creation(self):
        msg = Message.objects.create(
            sender=self.user,
            conversation=self.conversation,
            message_body="Hello test"
        )
        self.assertEqual(msg.message_body, "Hello test")

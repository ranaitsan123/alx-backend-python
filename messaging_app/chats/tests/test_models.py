from django.test import TestCase
from chats.models import User, Conversation, Message


class UserModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", password="pass123")
        self.assertIsNotNone(user.user_id)
        self.assertEqual(user.role, "guest")


class ConversationModelTests(TestCase):
    def test_conversation_creation(self):
        user1 = User.objects.create(email="a@example.com", password="123")
        user2 = User.objects.create(email="b@example.com", password="123")

        convo = Conversation.objects.create()
        convo.participants.add(user1, user2)

        self.assertEqual(convo.participants.count(), 2)


class MessageModelTests(TestCase):
    def test_message_creation(self):
        user = User.objects.create(email="test@example.com", password="pass")
        convo = Conversation.objects.create()
        convo.participants.add(user)

        msg = Message.objects.create(
            sender=user,
            conversation=convo,
            message_body="Hello"
        )

        self.assertEqual(msg.message_body, "Hello")
        self.assertEqual(msg.sender, user)

from rest_framework.test import APITestCase
from rest_framework import status
from chats.models import User, Conversation


class APITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="password123"
        )

        # Login to get JWT token
        response = self.client.post('/api/auth/login/', {
            "email": "test@example.com",
            "password": "password123"
        })

        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_create_conversation(self):
        response = self.client.post('/api/conversations/', {})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_send_message(self):
        conv = Conversation.objects.create()
        conv.participants.add(self.user)

        response = self.client.post(f'/api/conversations/{conv.conversation_id}/send_message/', {
            "sender_id": str(self.user.user_id),
            "message_body": "Hello world"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)

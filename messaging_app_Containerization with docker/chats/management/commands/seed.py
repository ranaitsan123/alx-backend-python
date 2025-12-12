from django.core.management.base import BaseCommand
from faker import Faker
from chats.models import User, Conversation, Message
import random


class Command(BaseCommand):
    help = "Seed database with fake users, conversations and messages"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create users
        users = []
        for _ in range(5):
            user = User.objects.create_user(
                email=fake.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                role="guest"
            )
            users.append(user)

        # Create conversations + messages
        for _ in range(3):
            conv = Conversation.objects.create()
            conv.participants.add(*random.sample(users, 2))

            # Messages
            for _ in range(5):
                Message.objects.create(
                    sender=random.choice(users),
                    conversation=conv,
                    message_body=fake.text()
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

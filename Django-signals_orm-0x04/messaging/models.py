from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    unread = UnreadMessagesManager()

    edited = models.BooleanField(default=False)  # Task 1
    parent_message = models.ForeignKey("self", null=True, blank=True,
                                       related_name="replies", on_delete=models.CASCADE)  # Task 3
    read = models.BooleanField(default=False)  # Task 4

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"Notification for {self.user}"

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    old_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

def get_thread(message):
    replies = message.replies.all().select_related("sender", "receiver")
    thread = []

    for reply in replies:
        thread.append(reply)
        thread.extend(get_thread(reply))

    return thread

class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.filter(receiver=user, read=False).only("id", "content", "timestamp")

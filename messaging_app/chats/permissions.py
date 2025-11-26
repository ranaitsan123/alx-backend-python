from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Allow only participants of a conversation to view or modify its messages.
    """

    def has_object_permission(self, request, view, obj):
        # If obj is a message → get its conversation
        conversation = getattr(obj, "conversation", obj)

        # Only allow access if the user is in the conversation
        return request.user in conversation.participants.all()

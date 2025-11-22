from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        # If obj is Message → check obj.conversation
        if hasattr(obj, "conversation"):
            conversation = obj.conversation
        else:
            conversation = obj  # obj is a Conversation

        return user in conversation.participants.all()

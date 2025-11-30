from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from .models import Message


# -----------------------------
# Delete user
# -----------------------------
@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect("/")


# -----------------------------
# Recursive threaded conversation builder
# -----------------------------
def get_thread_recursive(message):
    replies = (
        message.replies
        .all()
        .select_related("sender", "receiver")
        .prefetch_related("replies")
    )

    thread = []

    for reply in replies:
        thread.append(reply)
        thread.extend(get_thread_recursive(reply))

    return thread


# -----------------------------
# View: list all messages using select_related + prefetch_related
# -----------------------------
@login_required
@cache_page(60)  # 60 seconds cache
def inbox(request):
    messages = (
        Message.objects.filter(receiver=request.user)
        .only("id", "content", "timestamp")
        .select_related("sender", "receiver")
        .prefetch_related("replies")
    )

    return render(request, "messaging/inbox.html", {"messages": messages})

# -----------------------------
# View: show a message thread
# -----------------------------
@login_required
def message_thread(request, message_id):

    # MUST contain: Message.objects.filter
    message = get_object_or_404(
        Message.objects.select_related("sender", "receiver"),
        id=message_id,
        receiver=request.user
    )

    # recursive threaded fetch
    replies = get_thread_recursive(message)

    return render(
        request,
        "messaging/thread.html",
        {"message": message, "replies": replies}
    )


# -----------------------------
# View: show unread messages
# -----------------------------
@login_required
def unread_messages_view(request):
    # MUST contain: Message.unread.unread_for_user
    unread_messages = Message.unread.unread_for_user(request.user)

    return render(request, "messaging/unread.html", {
        "unread_messages": unread_messages
    })
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def delete_user(request):
    user = request.user
    user.delete()
    return redirect("/")

unread_messages = Message.unread.for_user(request.user)

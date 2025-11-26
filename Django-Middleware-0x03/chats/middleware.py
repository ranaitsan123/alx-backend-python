# chats/middleware.py
from datetime import datetime
import logging
import time
from django.http import HttpResponseForbidden, JsonResponse

# Request Logger Setup
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("requests.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "AnonymousUser"
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        return self.get_response(request)


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        if 18 <= current_hour < 21:
            return HttpResponseForbidden("Chat access is restricted between 6 PM and 9 PM.")

        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_record = {}

    def __call__(self, request):
        if request.method == "POST" and "chats" in request.path:
            user_ip = request.META.get("REMOTE_ADDR")
            now = time.time()
            window = 60
            limit = 5

            if user_ip not in self.message_record:
                self.message_record[user_ip] = []

            self.message_record[user_ip] = [
                t for t in self.message_record[user_ip] if now - t < window
            ]

            if len(self.message_record[user_ip]) >= limit:
                return JsonResponse(
                    {"error": "Rate limit exceeded. Max 5 messages per minute."},
                    status=429
                )

            self.message_record[user_ip].append(now)

        return self.get_response(request)


class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_paths = ['/chats/admin/', '/chats/moderate/']

        if any(request.path.startswith(p) for p in protected_paths):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required.")

            role = getattr(request.user, "role", "user")

            if role not in ["admin", "moderator"]:
                return HttpResponseForbidden("Permission denied. Admin/Moderator only.")

        return self.get_response(request)

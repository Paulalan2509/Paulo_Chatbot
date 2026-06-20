import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

from .models import ChatLog
from utils import get_response, sanitize_input


def chat_page(request):
    """
    Render the main chat page on initial page load.

    This runs exactly once per browser visit (or refresh) — every
    message sent afterward goes through send_message() below via AJAX,
    without reloading this page.
    """
    return render(request, 'chatbot/chat.html')


@csrf_protect
@require_http_methods(["POST"])
def send_message(request):
    """
    Handle a single chat message sent via AJAX (JavaScript fetch).

    Receives JSON like {"message": "hello"}, processes it through the
    same response logic as Phase 1's console bot, logs the exchange to
    MySQL, and returns JSON like {"response": "Hi there!"}.

    @require_http_methods(["POST"]) rejects GET requests with a 405
    error — there's no reason to "visit" this URL directly in a browser,
    it only makes sense as a POST target from JavaScript.
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid request format."}, status=400)

    raw_message = data.get("message", "")
    user_message = sanitize_input(raw_message)

    if not user_message:
        return JsonResponse({"error": "Message cannot be empty."}, status=400)

    bot_response = get_response(user_message)

    # Persist the exchange — this is what Phase 4B's analytics will read from later
    ChatLog.objects.create(
        user_message=user_message,
        bot_response=bot_response,
    )

    return JsonResponse({"response": bot_response})
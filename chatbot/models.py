from django.db import models


class ChatLog(models.Model):
    """
    Represents a single user message and the bot's response.

    Each row is one exchange: what the user typed, what the bot replied,
    and when it happened. This is the foundation for the analytics phase
    later (Phase 4B) — query frequency, response patterns, etc. all read
    from this table.
    """

    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']  # Most recent messages first by default

    def __str__(self):
        # Truncate long messages so Django admin list views stay readable
        preview = self.user_message[:50]
        return f"{preview}... ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"
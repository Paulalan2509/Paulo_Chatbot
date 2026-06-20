"""
Core chatbot logic: greeting generation, input sanitization, and response matching.
"""

from datetime import datetime
from responses import RESPONSES

MAX_INPUT_LENGTH = 500


def greet_user() -> str:
    """
    Generate a time-appropriate greeting based on the current hour.

    Returns:
        A greeting string ("Good morning!", "Good afternoon!", or "Good evening!").
    """
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning! I'm Paulo, your virtual assistant."
    elif hour < 18:
        return "Good afternoon! I'm Paulo, your virtual assistant."
    return "Good evening! I'm Paulo, your virtual assistant."


def sanitize_input(text: str) -> str:
    """
    Clean raw user input before processing.

    Strips leading/trailing whitespace, removes non-printable control
    characters, and enforces a maximum length to prevent abuse.

    Args:
        text: Raw user input string.

    Returns:
        Sanitized string, capped at MAX_INPUT_LENGTH characters.
    """
    if not isinstance(text, str):
        return ""

    cleaned = text.strip()
    # Remove control characters (e.g. null bytes, escape sequences) but keep normal punctuation
    cleaned = "".join(char for char in cleaned if char.isprintable())
    return cleaned[:MAX_INPUT_LENGTH]


def get_response(user_input: str) -> str:
    """
    Match user input against known keywords and return an appropriate response.

    Falls back to date/time handling, then a default "didn't understand" message
    if no keyword matches.

    Args:
        user_input: Sanitized user input string.

    Returns:
        The chatbot's response string.
    """
    normalized = user_input.lower().strip()

    if not normalized:
        return "Please enter something so I can help you."

    for keyword, response in RESPONSES.items():
        if keyword in normalized:
            return response

    if "time" in normalized:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    if "date" in normalized:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

    return "Sorry, I didn't understand that. Type 'help' to see what I can do."

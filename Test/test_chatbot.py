"""
Unit tests for Paulo Chatbot - Phase 1.

Run with: pytest test_chatbot.py -v
"""

import sys
import os

# Allow imports from the parent directory (project root) when running from Test/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils import get_response, sanitize_input, greet_user


class TestGetResponse:
    """Tests for keyword matching and fallback logic in get_response()."""

    def test_greeting_keyword(self):
        assert "Hello" in get_response("hello")

    def test_keyword_case_insensitive(self):
        assert get_response("HELLO") == get_response("hello")

    def test_keyword_within_sentence(self):
        # Keyword should match even when embedded in a longer phrase
        result = get_response("hi there, how are you")
        assert "Hi there" in result

    def test_unknown_input_returns_fallback(self):
        response = get_response("asdfghjkl")
        assert "didn't understand" in response.lower()

    def test_empty_input_after_strip(self):
        response = get_response("   ")
        assert "enter something" in response.lower()

    def test_time_request(self):
        response = get_response("what time is it")
        assert "time is" in response.lower()

    def test_date_request(self):
        response = get_response("what's the date today")
        assert "date is" in response.lower()

    def test_bye_keyword_returns_goodbye_response(self):
        # Note: in main.py, "bye" is intercepted as an exit command before
        # reaching get_response(). This test confirms get_response()'s own
        # behavior in isolation.
        response = get_response("bye")
        assert "goodbye" in response.lower()


class TestSanitizeInput:
    """Tests for input sanitization."""

    def test_strips_whitespace(self):
        assert sanitize_input("  hello  ") == "hello"

    def test_truncates_long_input(self):
        long_text = "a" * 1000
        result = sanitize_input(long_text)
        assert len(result) == 500

    def test_removes_non_printable_characters(self):
        text_with_control_char = "hello\x00world"
        result = sanitize_input(text_with_control_char)
        assert "\x00" not in result

    def test_non_string_input_returns_empty(self):
        assert sanitize_input(None) == ""
        assert sanitize_input(123) == ""

    def test_empty_string(self):
        assert sanitize_input("") == ""


class TestGreetUser:
    """Tests for the time-based greeting function."""

    def test_returns_valid_greeting(self):
        greeting = greet_user()
        valid_greetings = ("Good morning", "Good afternoon", "Good evening")
        assert any(greeting.startswith(g) for g in valid_greetings)

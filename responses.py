"""
Keyword-to-response mapping for Paulo Chatbot.

Each key is a lowercase keyword/phrase to match against user input.
Order matters only in that the first matching keyword wins (see utils.get_response),
so keep more specific phrases above more general ones if overlap occurs.
"""

RESPONSES = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! How can I assist you?",
    "help": "I can answer questions, tell you the time/date, or just chat. Type 'exit' to quit.",
    "name": "I'm Paulo, your virtual assistant. How can I help?",
    "who are you": "I'm Paulo, a chatbot here to assist you.",
    "thanks": "You're welcome! Anything else I can help with?",
    "thank you": "You're welcome! Let me know if you need anything else.",
    "bye": "Goodbye! Have a great day.",
    "goodbye": "Goodbye! Take care.",
}

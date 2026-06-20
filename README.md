# Paulo Chatbot — Phase 1: Console Application

A modular, console-based chatbot built in Python as the foundation phase of a larger multi-phase project (Console → Web → Voice → Customer Service/AI).

## Status

✅ Phase 1 complete — tested and passing.

## Features

- Keyword-based response matching (case-insensitive)
- Time-of-day-aware greeting on startup
- Dynamic responses for current time and date requests
- Input sanitization (strips control characters, caps length at 500 chars)
- Graceful exit via `exit`, `quit`, or `bye`
- Specific exception handling (`KeyboardInterrupt`, `EOFError`, `TypeError`/`ValueError`) rather than a catch-all
- Fallback response for unrecognized input
- Full pytest unit test suite (14 tests)
- PEP8 compliant (verified with `flake8`)

## Project Structure

```
Paulo_Chatbot/
├── main.py              # Entry point — interaction loop
├── utils.py             # Core logic: greeting, sanitization, response matching
├── responses.py         # Keyword-to-response dictionary
├── Test/
│   └── test_chatbot.py  # pytest unit tests
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/Paulalan2509/Paulo_Chatbot.git
   cd Paulo_Chatbot
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```
python main.py
```

Example session:
```
Good evening! I'm Paulo, your virtual assistant.
You: hello
Bot: Hello! How can I help you today?
You: what time is it
Bot: The current time is 22:21:47.
You: bye
Bot: Goodbye!
```

## Running Tests

```
pytest Test/test_chatbot.py -v
```

All 14 tests should pass, covering keyword matching, sanitization, edge cases, and the greeting function.

## Linting

```
flake8 main.py utils.py responses.py --max-line-length=100
```

## Known Limitations (by design, for this phase)

- Matching is simple substring keyword matching — no fuzzy matching or NLP yet (planned for Phase 4C)
- No persistence — conversations are not logged or saved (planned for Phase 2 onward)
- No web or voice interface yet (Phases 2 and 3)

## Roadmap

| Phase | Description |
|---|---|
| **1 (this phase)** | Console chatbot |
| 2 | Django web chatbot with Tailwind UI |
| 2B | Auth, sessions, admin dashboard |
| 3 | Voice/speech recognition |
| 4A | MySQL + CRUD for customer service |
| 4B | Analytics dashboard |
| 4C | AI/NLP integration (OpenAI) |
| 5 | Testing & deployment |

## License

TBD
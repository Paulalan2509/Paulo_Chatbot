"""
Paulo Chatbot - Phase 1: Console Application

Entry point for the console-based chatbot. Handles the main interaction loop,
input validation, and graceful error handling.
"""

from utils import greet_user, get_response, sanitize_input

EXIT_COMMANDS = {"exit", "quit", "bye"}


def main() -> None:
    """Run the main chatbot interaction loop."""
    print(greet_user())

    while True:
        try:
            raw_input_text = input("You: ")
            user_input = sanitize_input(raw_input_text)

            if not user_input:
                print("Bot: Please enter something.")
                continue

            if user_input.lower() in EXIT_COMMANDS:
                print("Bot: Goodbye!")
                break

            response = get_response(user_input)
            print("Bot:", response)

        except KeyboardInterrupt:
            print("\nBot: Session terminated.")
            break

        except EOFError:
            # Happens if input stream is closed unexpectedly (e.g. piped input ends)
            print("\nBot: Input stream closed. Goodbye!")
            break

        except (TypeError, ValueError) as e:
            # Errors from malformed input processing
            print("Bot: I couldn't process that input. Please try again.")
            print(f"[debug] {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

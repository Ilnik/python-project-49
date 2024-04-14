import prompt
from typing import Callable


def process_game(
    question_generator: Callable[[], tuple[str, str]],
    start_game_text: str,
):
    """
    Function to process a game
    : param start_game_text: Entry text
    : param question_generator: Callable object to generate objects and answers
    """

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(start_game_text)

    for _ in range(3):
        question, answer = question_generator()

        result = prompt.string(f"Question: {question}\nYour answer: ").lower()
        if result != answer:
            print(f"This answer is incorrect!\nLet's try again, {name}")
            break

        print("Correct!")

    print("Congratulations!")

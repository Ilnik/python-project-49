from new_random import get_random_number_from_range
from main import process_game
from typing import Tuple

START_WELCOME_TEXT = 'Answer "yes" if the number is even, otherwise answer "no"'


def generate_even_question() -> Tuple[str, str]:
    number = get_random_number_from_range()
    answer = "yes" if number % 2 == 0 else "no"
    return str(number), answer


def play():
    process_game(
        question_generator=generate_even_question,
        start_game_text=START_WELCOME_TEXT
    )

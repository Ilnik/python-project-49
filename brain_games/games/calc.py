from typing import Tuple
import random
from new_random import get_random_number_from_range
from main import process_game

START_WELCOME_TEXT = "What is the result of the expression?"


def is_calc() -> Tuple[str, str]:
    question = (
        f"{get_random_number_from_range()} "
        f"{random.choice(['+', '-', '*'])} "
        f"{get_random_number_from_range()}"
    )
    answer = str(eval(question))
    return question, answer


def play():
    process_game(question_generator=is_calc, start_game_text=START_WELCOME_TEXT)


play()

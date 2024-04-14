from main import process_game
from typing import Tuple
import random
from new_random import get_random_number_from_range


START_WELCOME_TEXT = "What number is missing in the progression?"


def random_progression_generation() -> Tuple[str, str]:
    start = get_random_number_from_range()
    step = get_random_number_from_range()
    length = get_random_number_from_range()
    progression = [start + i * step for i in range(length)]
    hidden_element_index = random.randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    progression[hidden_element_index] = ".."
    answer = hidden_element
    return str(progression), str(answer)


def play():
    process_game(
        question_generator=random_progression_generation,
        start_game_text=START_WELCOME_TEXT,
    )

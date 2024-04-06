from new_random import get_random_number_from_range
from main import process_game
from typing import Tuple
import random


START_WELCOME_TEXT = 'What number is missing in the progression?'


def is_progression() -> Tuple[str, str]:
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(8, 10)
    progression = [start + i * step for i in range(length)]
    hidden_element_index = random.randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    progression_with_hidden = ['..' if i == hidden_element_index else elem for i, elem in enumerate(progression)]
    answer = hidden_element
    return str(progression_with_hidden), str(answer)


def play():
    process_game(question_generator=is_progression, start_game_text=START_WELCOME_TEXT)


play()
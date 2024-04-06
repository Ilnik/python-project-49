from new_random import get_random_number_from_range
from main import process_game
from typing import Tuple


START_WELCOME_TEXT = 'Find the greatest common divisor of given numbers.'


def is_gcd() -> Tuple[str, str]:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1, num2 = get_random_number_from_range(), get_random_number_from_range()
    number = f"{num1} {num2}"
    answer = gcd(num1, num2)
    return number, str(answer)


def play():
    process_game(question_generator=is_gcd, start_game_text=START_WELCOME_TEXT)


play()

from typing import Tuple
from new_random import get_random_number_from_range
from main import process_game


START_WELCOME_TEXT = ('Answer "yes" if the number is prime. '
                      'Otherwise answer "no".')


def is_prime() -> Tuple[str, str]:
    def prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    number = get_random_number_from_range()
    answer = "yes" if prime(number) else "no"
    return str(number), answer


def play():
    process_game(question_generator=is_prime,
                 start_game_text=START_WELCOME_TEXT)


play()

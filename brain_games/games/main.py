import prompt
from typing import Callable
from even import is_even
from calc import is_calc
from gcd import is_gcd
from prime import is_prime
from progression import is_progression


def process_game(function: Callable[[], tuple[str, str]]):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    answer_count = 0
    for _ in range(3):
        question, answer, user_answer = function()
        print(question)

        if user_answer != answer:
            print(
                f"{user_answer} is the wrong answer ;(. "
                f"Correct answer was {answer}.\n"
                f"Let's try again, {name}!"
            )
            return
        print("Correct!")
        answer_count += 1
    print("Congratulations!")


if __name__ == "__main__":
    process_game(is_even)

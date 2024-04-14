from typing import Tuple
import random
from new_random import get_random_number_from_range
from main import process_game

START_WELCOME_TEXT = "What is the result of the expression?"


def calculator() -> Tuple[str, str]:
    def calculate_expression(expression: str) -> int:
        num1, operator, num2 = expression.split()
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2

    question = (
        f"{get_random_number_from_range} "
        f"{random.choice(['+', '-', '*'])} "
        f"{get_random_number_from_range}"
    )
    answer = str(calculate_expression(question))
    return question, answer


def play():
    process_game(question_generator=calculator, start_game_text=START_WELCOME_TEXT)

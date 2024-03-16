import random


def generate_expression():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    expression = f"{num1} {operator} {num2}"
    return expression


def evaluate_expression(expression):
    return eval(expression)


def is_calc():
    message = "What is the result of the expression?"
    question = f"Question: {generate_expression()}"
    user_answer = input("Your answer: ").lower()
    answer = evaluate_expression(
        generate_expression()
    ) and user_answer == evaluate_expression(generate_expression())
    return question, answer, message

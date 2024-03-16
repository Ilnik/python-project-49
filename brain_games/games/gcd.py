import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_gcd():
    message = "Find the greatest common divisor of given numbers."
    question = f"Question: {random.randint(1, 20)} {random.randint(1, 20)}"
    user_answer = input("Your answer: ").lower()
    answer = gcd(random.randint(1, 20), random.randint(1, 20)) \
        and user_answer == gcd(
        random.randint(1, 20), random.randint(1, 20)
    )
    return question, answer, message

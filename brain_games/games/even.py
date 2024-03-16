import random


def even(number):
    return number % 2 == 0


def is_even():
    message = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_number = random.randint(1, 100)
    question = f"Question: {random_number}"
    user_answer = input("Your answer: ").lower()
    answer = even(random_number) == (user_answer == "yes") \
        or not even(random_number) == (user_answer == "no")
    return question, answer, message

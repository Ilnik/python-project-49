import random


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime():
    message = 'Answer "yes" if the number is prime. Otherwise answer "no".'
    random_number = random.randint(1, 100)
    question = f"Question: {random_number}"
    user_answer = input("Your answer: ").lower()
    answer = (prime(random_number) == (user_answer == "yes")) \
        or (not prime(random_number) == (user_answer == "no"))
    return question, answer, message

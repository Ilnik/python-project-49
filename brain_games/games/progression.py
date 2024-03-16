import random


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    length = random.randint(8, 10)
    return [start + i * step for i in range(length)]


def hidden_ran_elem(progression):
    hidden_element_index = random.randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    progression_with_hidden = ['..' if i == hidden_element_index else elem
                               for i, elem in enumerate(progression)]
    return progression_with_hidden, hidden_element


def is_progression():
    message = 'What number is missing in the progression?'
    progression, hidden_element = hidden_ran_elem(generate_progression())
    question = "Question:", ' '.join(map(str, progression))
    user_answer = input("Your answer: ").lower()
    answer = hidden_element == user_answer
    return question, answer, message

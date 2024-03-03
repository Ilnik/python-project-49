import random, prompt



def is_even(number):
    return number % 2 == 0


def play():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    username = name.split("? ")[1::]

    correct_answers_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while correct_answers_count < 3:
        random_number = random.randint(1, 100)


        print(f"Question: {random_number}")

        user_answer = input(f"Your answer: ").lower()

        if (is_even(random_number) and user_answer == 'yes') or \
                (not is_even(random_number) and user_answer == 'no'):
            print("Correct!")
            correct_answers_count += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name} !")
            correct_answers_count = 0
            continue

    print(f"Congratulations, {name}!")


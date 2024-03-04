import random
import prompt

# Function that generates random progression.


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    length = random.randint(8, 10)
    return [start + i * step for i in range(length)]


# Function that generates random hidden element and change it to "..".
def hidden_ran_elem(progression):
    hidden_element_index = random.randint(0, len(progression) - 1)
    hidden_element = progression[hidden_element_index]
    progression_with_hidden = ['..' if i == hidden_element_index else elem
                               for i, elem in enumerate(progression)]
    return progression_with_hidden, hidden_element


# Main function play().
def play():
    # This is greetings of user.
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Counter of the right answers. Now it's on 0 mark.
    correct_answers_count = 0
    print('What number is missing in the progression?')

    # Cycle of questioning user. 3 right answers = victory, if not - try again.
    while correct_answers_count < 3:
        progression, hidden_element = hidden_ran_elem(generate_progression())
        print("Question: ", ' '.join(map(str, progression)))

        # Integer input of user answer for right comparison in the next
        # iterations.
        user_answer = int(input("Your answer: "))

        if hidden_element == user_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {hidden_element}.")
            print(f"Let's try again, {name}!")
            correct_answers_count = 0
            exit()

    print(f"Congratulations, {name}!")

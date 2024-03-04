import random
import prompt


# Function that generates random expression as integer.


def generate_expression():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1}{operator}{num2}"
    return expression


# Function that evaluate random expression as integer.
# Now we can use it further.


def evaluate_expression(expression):
    result = eval(expression)
    return result


# Main function play().


def play():
    # This is greetings of user.
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Counter of the right answers. Now it's on 0 mark.
    correct_answers_count = 0
    print('What is the result of the expression?')

    # Cycle of questioning user. 3 right answers = victory, if not - try again.
    while correct_answers_count < 3:
        # Putting evaluate_expression function into variable math_expression
        # for further use in cycle.
        math_expression = generate_expression()

        # Correct answer generating.
        correct_answer = evaluate_expression(math_expression)
        print(f"Question: {math_expression}")

        # Integer input of user answer for right comparison in the next
        # iterations.
        user_answer = int(input("Your answer: "))

        if correct_answer == user_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            correct_answers_count = 0
            exit()

    print(f"Congratulations, {name}!")

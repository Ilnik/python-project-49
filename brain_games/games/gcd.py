import random
import prompt

# Function that generates random number.


def ganerate_random_numbers():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    return num1, num2


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Main function play().
def play():
    # This is greetings of user.
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Counter of the right answers. Now it's on 0 mark.
    correct_answers_count = 0
    print('Find the greatest common divisor of given numbers.')

    # Cycle of questioning user. 3 right answers = victory, if not - try again.
    while correct_answers_count < 3:
        num1, num2 = ganerate_random_numbers()
        correct_answer = gcd(num1, num2)
        print(f"Question: {num1} {num2}")

        # Integer input of user answer for right comparison in the next
        # iterations.
        user_answer = int(input("Your answer: "))

        if correct_answer == user_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}.")
            print(f"Let's try again, {name} !")
            correct_answers_count = 0
            exit()

    print(f"Congratulations, {name}!")

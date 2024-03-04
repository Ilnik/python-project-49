import random
import prompt

# Function that is checking for prime number.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Main function play().
def play():
    # This is greetings of user.
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Counter of the right answers. Now it's on 0 mark.
    correct_answers_count = 0
    print('Answer "yes" if the number is prime, otherwise answer "no"')

    # Cyrcle of questionin user. 3 right answers = victory, if not - try again.
    while correct_answers_count < 3:
        # Creating a random number.
        random_number = random.randint(1, 100)

        print(f"Question: {random_number}")
        # User answer as string (yes or no in the lowercase)
        user_answer = input("Your answer: ").lower()
        # Counting right answers and looping cycle if counter less than 3.
        if (is_prime(random_number) and user_answer == 'yes') or \
                (not is_prime(random_number) and user_answer == 'no'):
            print("Correct!")
            correct_answers_count += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name} !")
            correct_answers_count = 0

    print(f"Congratulations, {name}!")

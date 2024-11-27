import random  # Import the 'random' module to generate random numbers

def number_guessing_game():
    print("Game is starting...")  # Add this line to check if the code is running
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Initialize the number of attempts to 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()

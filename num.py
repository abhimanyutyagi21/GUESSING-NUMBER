import random

num_to_guess = random.randint(1, 100)

while True:  # Use a loop to keep asking until the correct guess
    try:
        guess = int(input("Guess the Number between 1 and 100: "))
        if guess < num_to_guess:
            print("Too Low!")
        elif guess > num_to_guess:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number.")
            break  # Exit the loop when the guess is correct
    except ValueError:
        print("Please enter a valid number.")

import random
def start_game():
    print("Welcome to the Number Guessing Game comrade!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess:
            print("Congratulations comrade! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high comrade! Try again.")
        elif guess < number_to_guess:
            print("Too low comrade! Try again.")  
        continue
    print("Game Over. Thanks for playing comrade!")
start_game()

# logic error, ln 14 if to elif

#

#

#
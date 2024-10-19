import random

def guess_number_game():
    # Step 1: Randomly generate a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    # Step 2: Loop until the player guesses the correct number
    while not guessed:
        # Step 3: Take input from the user
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Step 4: Compare the guess with the actual number
        if user_guess > number_to_guess:
            print("Too high! Try again.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            guessed = True

# Call the function to start the game
guess_number_game()

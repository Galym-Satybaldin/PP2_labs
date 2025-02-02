import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    
    # Randomly choose a secret number between 1 and 20.
    secret_number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    guesses = 0 # guess counter
    
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1  
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            # Correct guess: break out of the loop.
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()

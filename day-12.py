import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")

number = random.randint(1, 101)
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

game_over = False
while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess:\n"))
    if guess == number:
        print(f"You got it! The answer was {number}")
        game_over = True
    elif guess < number:
        print("Your guess is too low.")
        attempts -= 1
    elif guess > number:
        print("Your guess is too high.")
        attempts -= 1
    else:
        print("Enter a number between 1 and 100.")

    if attempts == 0:
        print("Sorry, you ran out of guesses.")
        game_over = True


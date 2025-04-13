#FOR LOOP:

# Pattern 1: Counting Numbers
print("Counting Numbers from 1 to 10")
for i in range(1, 11):
    print(i, end=" ")
print("\n")  

# Pattern 2: Multiplication Table for 5
print("Multiplication Table for 5")
for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

#WHILE LOOP:

#GUESS THE NUMBER GAME:

secret_number = 27

# Counter for number of guesses
guess_count = 0

print("🎯 Welcome to the Number Guessing Game!")
print("Guess the secret number between 1 and 50.")

while True:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it right in {guess_count} attempts.")
        break

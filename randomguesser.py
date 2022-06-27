import random

# get the start of range
while True:
    i1 = input("Enter the start of the range: ")
    try:
        start = int(i1)
        break
    except Exception:
            print("Please enter a valid number.")

while True:
    i2 = input("Enter the end of the range: ")
    try:
        end = int(i2)
        if start <= end: # here Idk: Are they allowed to be the same?
            break
        else:
            raise Exception("Please enter a valid number.")
    except Exception:
        print("Please enter a valid number.")

# I don't need to create the list first (and add plus one 1 to the end for inclusivity)
# because the random int method already does that for me (inclusive)

winner = random.randint(start, end)

guess_count = 0
while True:
    i3 = input("Guess a number: ")
    try:
        guesser = int(i3)
        guess_count += 1
        if guesser == winner:
            if guess_count == 1:
                print(f"You guessed the number in {guess_count} attempt")
            else:
                print(f"You guessed the number in {guess_count} attempts")
            break
        else:
            continue
    except Exception:
        print("Please enter a valid number.")
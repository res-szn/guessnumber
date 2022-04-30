import random

n = random.randint (1,20)
print("I am thinking of a number between 1 and 20")

running = True
while running:
    guess_str = input("Take a wild guess ")
    guess = int (guess_str)
    if guess == n:
        print("Congratulations, that is correct!")
        running = False
    elif guess < n:
        print("Try a larger number")
    else:
        print("Try a smaller number")
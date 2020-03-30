import  random

number = random.randint(1, 100)
print("guess the number between 1 to 100")

turns = 0
while turns <= 3:
    guess = int(input())

    if guess == number:
        print("yay! That's a correct guess!!")
        break
    elif guess < number:
        print("guess a higher number than this")
    else:
        print("the guess is too high")

    turns += 1

if turns > 3:
    print("you loose:( Correct guess is", number)



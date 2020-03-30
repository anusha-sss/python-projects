import  random

number = random.randint(1, 100)
print("guess the number between 1 to 100")

turns = 0
chances = 0
while turns <= 1:
    guess = int(input())
    new1 = abs(number - guess)
    if guess == number:
        print("yay! That's a correct guess!!")
        break
    elif guess < number:
        print("guess a higher number than this")
    else:
        print("guess a lower number than this")

        while chances <=4:
            new2 = abs(number-guess)
            if new2 < new1 :
                print("you are closer to the guess")
            elif new2 == new1:
                print("you are closer to the guess")
            else:
                print("you are farther from the guess")
            chances += 1
        if turns > 4:
                print("you lost:( Correct guess is", number)

    turns += 1





import random

print("Number guessing Game")
print("Guess a number between 1 and 9")

randomNumber = random.randrange(1,9)
print(randomNumber)


guess = int(input("Enter your guess: "))


while guess  != randomNumber:
    
    if(guess > randomNumber):
        print("Your guess was too high: Guess a number lower than " + str(guess))
        guess = int(input("Enter your guess: "))
    elif(guess < randomNumber):
        print("Your guess was too low: Guess a number higher than " + str(guess))
        guess = int(input("Enter your guess: "))
    else:
        print("What u have entered is not a number: Please enter a number")
        guess = int(input("Enter your guess: "))

if(guess == randomNumber):
        print(" Yes!, You got it right! The number was " + str(randomNumber))
    

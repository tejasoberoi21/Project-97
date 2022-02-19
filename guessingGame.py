import random

correctAnswer = random.randint(1,20)
userAnswer = 0
guesses = 1
while(correctAnswer != userAnswer and guesses <= 5):
    userAnswer = int(input("Guess a number between 1 and 20: "))
    if(userAnswer < correctAnswer):
        print("Your guess was too low, you have:",(5-guesses), "attempts left")
        if(guesses == 5):
            print("You lost")
            print("The correct value is: ", correctAnswer)
    elif(userAnswer > correctAnswer):
        print("Your guess was too high, you have:",(5-guesses), "attempts left")
        if(guesses == 5):
            print("You lost")
            print("The correct value is: ", correctAnswer)
    else:
        print("Congratulations, you guessed the correct number in", (guesses), "attempts!!!")
    guesses+=1

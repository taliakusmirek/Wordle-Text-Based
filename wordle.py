import random

wordle = ["budge", "reach", "brush","straw"]
# feel free to add more words if you wish! I left it at a limited amount for testing purposes. :)
guessCount = 0

wordCorrect = random.choice(wordle)

while (guessCount <= 5):
    guess = input("Guess a word, you have five tries: ")
    correctWord = 0
    for i in range(len(guess)):
        # check if letter is in the right spot
        if guess[i] == wordCorrect[i]:
            print(guess[i], "is in the right spot")
            correctWord += 1
            # if the guess is completely correct
            if (correctWord == 5):
                print("You got the word! Congrats!")
                quit()
        # check if letter is in the word, just not in the right spot
        elif (guess[i].find(wordCorrect) != -1):
            print(guess[i], "is close!")
        # check if every letter is wrong
        elif (guess[i].find(wordCorrect) == -1):
            print(guess[i], "is not in the word!")

    guessCount +=1

print("You have used up your five guesses, better luck next time!")




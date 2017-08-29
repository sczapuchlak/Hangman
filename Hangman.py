#this program plays hangman with the user
import random


def getRandomWord():
    #using with open instead of open closes the file automatically at the end
    #of the statement
    with open("wordsForHangman.txt") as fileRead:
        wordList = list(fileRead)
    word = (random.choice(wordList).strip())
    return word

def welcomeUser():
    name = input("What is your name scalleywag?")
    print(" Welcome, "+ name + ", you will  have 9 chances to guess the "
    "letters in the word, or you will die in the gallows! Guess wisely. "
    "*Evil Laugh* ")
    return name

def playHangman():
   #get the random word of the game from the getRandomWord function
    wordOfTheGame = getRandomWord()
    listToDisplayDashes = []
   # use set to see if user already guessed. sets don't allow duplicate values
    lettersGuessed= set()
    letterInTheWord = set(wordOfTheGame)
    guess = 0
    print(wordOfTheGame)
     
    # make sure the user has guesses left, if not, the game is over
    # also make sure that there are letters left in the word for the user to guess

    while guess <= 6 and len(letterInTheWord)>0 :
        lettersGuessed = ''
        # make sure whatever the user enters is lowercase so there are no problems with typecase
        userGuess = input("Please enter a letter you think is in the word: ").lower()
        if userGuess in wordOfTheGame and userGuess not in lettersGuessed:
            print("One letter correct")
            lettersGuessed += ","+lettersGuessed
            print("Progress: ")




          #   playAgain = input("Sorry, you didn't guess the word. Would you like another life to try again? Press Y "
          # "yes or any other key to quit")


getRandomWord()
welcomeUser()
playHangman()




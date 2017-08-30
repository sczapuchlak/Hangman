#this program plays hangman with the user
#this website helped me a little bit, with showing me logic on how someone played a guessing game with letters
#http://www.practicepython.org/solution/2017/01/08/31-guess-letters-solutions.html
#Didn't need classes because working with words didn't call for it
#If I was working with multiple players and cards I could make a class for those

import random




def getRandomWord():
    #using with open instead of open closes the file automatically at the end
    #of the statement
    with open("wordsForHangman.txt") as fileRead:
        wordList = list(fileRead)
    word = (random.choice(wordList).strip())
    return word

def welcomeUser():
    #welcome the user!
    name = input("Hello! What is your name scalleywag?")
    choose = str("press enter to continue...")
    print("Welcome, "+ name + "!")
    input(choose)
    print('''
|───────────────────────────────────────────────────────────────────| 
|                  How to Play Hangman                     |
|───────────────────────────────────────────────────────────────────|
|  To Play Hangman, you must guess the word correctly     |
|  in the amount of tries listed. The amount of tries     |
|  will vary on how long your word is. You will have 1    |
|  less try than the length of the word. You can guess    |
|  only one letter at a time. For each wrong attempt,     |
|  you will add one body part to the noose. When the      |
   amount of tries runs out, you will die in the gallows. |
|_________________________________________________________|
 '''
)
    input(choose)
    print("Choose your letters wisely. *Evil Laugh* ")
    input(choose)
    return name


def playHangman():
    #clear the screen to make the game easier to read
    print("\n" * 5)
    # get the random word of the game from the getRandomWord function
    wordOfTheGame = getRandomWord()
    #this gives the user x number of attempts per game
    tries = len(wordOfTheGame)-1
    #set up the list for letters being guessed so if user has already guessed, it informs them
    lettersGuessed= []
    #set up the list for the word that is being guessed, with * for all unknowns
    wordThatIsBeingGuessed = []
    for letter in wordOfTheGame:
        wordThatIsBeingGuessed.append("*")

    # print(wordOfTheGame) this was for testing purposes only

    # make sure the user has guesses left, if not, the game is over
    # also make sure that there are letters left in the word for the user to guess

    while tries !=0 and "*" in wordThatIsBeingGuessed:
        #This adds the * for the blank spaces
        wordPutTogether = "".join(wordThatIsBeingGuessed)
        print(wordPutTogether)

        # make sure whatever the user enters is lowercase so there are no problems with typecase
        #use exception handling
        try:
            userGuess = input("Please enter a letter you think is in the word: ").lower()
        #exception handling on page 107 python book
        except:
            print("Something went wrong! Try again!")
        else:
            # tell the user if they have already guessed that letter and to guess again
            if userGuess in lettersGuessed:
                print("You have already guessed that letter! Please guess a different letter!")
                continue

            # make sure they enter a letter and nothing else/aren't being greedy with letters
            if not userGuess.isalpha() or len(userGuess) > 1:
                print("This is hangman! Do you even know how to play? Please enter ONE letter silly!")
                continue

        #add the users guesses to the letters guessed list
        lettersGuessed.append(userGuess)
        #check to see if the letter is in the word of the game
        for letter in range(len(wordOfTheGame)):
            #use an if statement if the users guess is in the letter of the game
            if userGuess == wordOfTheGame[letter]:
                #add the users letter to the word that is being guessed list
                wordThatIsBeingGuessed[letter]=userGuess
                #since the user is correct, they dont lose an attempt, but still need to know how many
                #attempts they have left
                print("You have " + str(tries) + " attempts left")

        if userGuess not in wordOfTheGame:
            #if the user is wrong, take an attempts away
            tries -= 1
            # tell the user how many attempts they have left
            print("You have " + str(tries) + " attempts left")
    #if they have no more stars left, they win the game
    if "*" not in wordThatIsBeingGuessed:
        print("You beat the game! You live another day!")
    #they ran out of stars
    else:
        print("You lost! The word was:"+ wordOfTheGame +" Na na na na boo boo! ")




          #   playAgain = input("Sorry, you didn't guess the word. Would you like another life to try again? Press Y "
          # "yes or any other key to quit")



def main():
    getRandomWord()
    welcomeUser()
    playHangman()
main()


# this program plays hangman with the user
# this website helped me a little bit, with showing me logic on how someone played a guessing game with letters
# http://www.practicepython.org/solution/2017/01/08/31-guess-letters-solutions.html
import random
import sys

class Hangman(object):

    def __init__(self):
        self.runGame()

    def runGame(self):
        self.welcomeUser()
        self.RandomizeWordList()
        self.getWordOfTheGame()
        self.playHangman()
        self.playAnotherTime()

    def welcomeUser(self):
        # welcome the user!
        name = input("Hello! What is your name scalleywag?")
        choose = str("press enter to continue...")
        print("Welcome, " + name + "!")
        input(choose)
        print('''
    |────────────────────────────────────────────|
    |                  How to Play Hangman                    |
    |────────────────────────────────────────────|
    |  To Play Hangman, you must guess the word correctly     |
    |  in the amount of tries listed. You will have a total   |
    |  of 6 tries. You may only guess only one letter at a    |
    |  at a time. For each wrong attempt, you will add one    |
    |  body part to the noose. When the amount of tries runs  |
    |  out, you will die in the gallows and be hung.          |
    |_________________________________________________________|
     '''
            )
        input(choose)
        print("Choose your letters wisely. *Evil Laugh* ")
        input(choose)
        return name


    def RandomizeWordList(self):
        # using with open instead of open closes the file automatically at the end
        # of the statement
        with open("wordsForHangman.txt") as fileRead:
            wordList = list(fileRead)
        word = (random.choice(wordList).strip())
        return word



    def getWordOfTheGame(self):
        # get the random word of the game from the getRandomWord function
        wordOfTheGame = self.RandomizeWordList()
        return wordOfTheGame


    def playHangman(self):
        word = self.getWordOfTheGame()
        # clear the screen to make the game easier to read
        print("\n" * 5)
        # this gives the user x number of attempts per game
        tries = 6
        # set up the list for letters being guessed so if user has already guessed, it informs them
        lettersGuessed = []
        # set up the list for the word that is being guessed, with * for all unknowns


        wordThatIsBeingGuessed = []
        for letter in word:
            wordThatIsBeingGuessed.append("*")

        # print(wordOfTheGame) this was for testing purposes only

        # make sure the user has guesses left, if not, the game is over
        # also make sure that there are letters left in the word for the user to guess

        while tries >= 0 and "*" in wordThatIsBeingGuessed:
            # This adds the * for the blank spaces
            wordPutTogether = "".join(wordThatIsBeingGuessed)
            print(wordPutTogether)

            # make sure whatever the user enters is lowercase so there are no problems with typecase
            # use exception handling
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

            # add the users guesses to the letters guessed list
            lettersGuessed.append(userGuess)
            # check to see if the letter is in the word of the game
            for letter in range(len(word)):
                # use an if statement if the users guess is in the letter of the game
                if userGuess == word[letter]:
                    #add the gallows pertaining to whatever try number they are on
                    self.gallows(tries)
                    print
                    "Progress: " + self.progressReport(userGuess, word , wordThatIsBeingGuessed)
                    print("Letter used: " + str(lettersGuessed))
                    print("You have " + str(tries) + " attempts left")
                    # add the users letter to the word that is being guessed list
                    wordThatIsBeingGuessed[letter] = userGuess


            if userGuess not in word:
                # add the gallows pertaining to whatever try number they are on
                self.gallows(tries)
                print("Progress: " + self.progressReport(userGuess, word , wordThatIsBeingGuessed))
                print("Letter used: " + str(lettersGuessed))
                print("You have " + str(tries) + " attempts left")
                # if the user is wrong, take an attempts away
                tries -= 1

        # if they have no more stars left, they win the game
        if "*" not in wordThatIsBeingGuessed:
            print("You beat the game! You live another day!")
        # they ran out of stars
        else:
            print("You lost! The word was:" + word + " Na na na na boo boo! ")

    # this will print how many guess the user has left and what they have guessed
    def progressReport(self, userGuess, word, wordThatIsBeingGuessed):
        i = 0
        while i < len(word):
            if userGuess == word[i]:
                wordThatIsBeingGuessed[i] = userGuess
                i += 1
            else:
                i += 1

        return "".join(wordThatIsBeingGuessed)

    #Ask the user if they want to play again!
    def playAnotherTime(self):
        again = input('Do you want to play again? Y for yes and anything else for no')
        if again =='y' or again=='Y':
            self.runGame()
        else:
            sys.exit(0)

    #create the gallows to show when user guesses correctly or incorrectly
    def gallows(self,tries):
            if tries == 0:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     / \     ")
                print("|             ")
            elif tries == 1:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     /       ")
                print("|             ")
            elif tries == 2:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|             ")
                print("|             ")
            elif tries == 3:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|      ")
                print("|             ")
                print("|             ")
            elif tries == 4:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|      |     ")
                print("|             ")
                print("|             ")
            elif tries == 5:
                print("_____      ")
                print("|    |      ")
                print("|    0      ")
                print("|             ")
                print("|             ")
                print("|             ")
            elif tries ==6:
                print("_____      ")
                print("|   |      ")
                print("|          ")
                print("|          ")
                print("|          ")
                print("|          ")

#Calls the program to run the first time!
Hangman()









# def hangman_graphic(self, guesses):
# 		if guesses == 0:
# 			print( "________      ")
# 			print ("|      |      ")
# 			print ("|             ")
# 			print ("|             ")
# 			print ("|             ")
# 			print ("|             ")
# 		elif guesses == 1:
# 			print ("________      ")
# 			print ("|      |      ")
# 			print ("|      0      ")
# 			print ("|             ")
# 			print ("|             ")
# 			print ("|             ")
# 		elif guesses == 2:
# 			print ("________      ")
# 			print ("|      |      ")
# 			print ("|      0      ")
# 			print ("|     /       ")
# 			print ("|             ")
# 			print ("|             ")
# 		elif guesses == 3:
# 			print (""________      ")
# 			print (""|      |      ")
# 			print (""|      0      ")
# 			print (""|     /|      ")
# 			print (""|             ")
# 			print (""|             ")
# 		elif guesses == 4:
# 			print (""________      ")
# 			print (""|      |      ")
# 			print (""|      0      ")
# 			print (""|     /|\     ")
# 			print (""|             ")
# 			print (""|             ")
# 		elif guesses == 5:
# 			print ("________      ")
# 			print ("|      |      ")
# 			print ("|      0      ")
# 			print ("|     /|\     ")
# 			print ("|     /       ")
# 			print ("|             ")
# 		else:
# 			print ("________      ")
# 			print ("|      |      ")
# 			print ("|      0      ")
# 			print ("|     /|\     ")
# 			print ("|     / \     ")
# 			print ("|             ")
# 			print ("The noose tightens around your neck, and you feel the"
# 			print ("sudden urge to urinate."
# 			print ("GAME OVER!"
# 			self.__init__()

# while guess <= 6 and len(letterInTheWord) > 0:
#
#     # make sure whatever the user enters is lowercase so there are no problems with typecase
#     userGuess = input("Please enter a letter you think is in the word: ").lower()
#
#     # check to see if the user already guessed that letter
#     if guess in lettersGuessed:
#         print("You already guessed that letter! Try again!")
#         continue
#
#     for char in wordOfTheGame:
#         if char in userGuess:
#             listToDisplayDashes.append(char.upper())
#             # print(listToDisplayDashes)
#
#     guess += 1
#     print(" ".join(listToDisplayDashes))
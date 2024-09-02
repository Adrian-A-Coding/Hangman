"""
Name: Adrian Aguilar
Date: 7/15/24
Assignment: Final Project
Last Updated:7/31/24
Planned Improvements: Creating player classes and allowing to play as 1 or 2 players
"""
#from Hangman_Player import Player
import random as rd
import os

WORDPATH = os.path.join(os.getcwd(), "wordBank.txt")
#PLAYERPATH = os.path.join(os.getcwd(), "player.txt")
WORDLIST = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog',
            'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose',
            'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon',
            'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel',
            'whale', 'wolf', 'wombat', 'zebra']
GUESSLIMIT = 6
TEST = ['wolf', 'wombat', 'zebra']


def readFile(filePath):
    if not os.path.exists(filePath):
        print('The file, ' + filePath + ' does not exist - cannot read it.')
        return ''

    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data

def display(misses, corrects):
    if not misses and not corrects:
        print("Incorrect: 0    Correct: 0")
    elif not misses:
        print("Incorrect: 0    Correct: ", len(corrects))
    elif not corrects:
        print("Incorrect:", len(misses), "   Correct: 0")
    else:
        print("Incorrect:", len(misses), "   Correct:", len(corrects))


def handleUserGuess(guess, secret, displayHolding, misses, corrects):
    #Checking for any error cases in the guess
    if len(guess) > 1:
        print("Please enter one letter at a time.")
        return
    elif not guess:
        print("Please try again, that wasn't a letter.")
        return
    elif ord(guess) < 97 or ord(guess) > 127:
        print("Please enter a letter between a-z.")
        return
    elif guess in misses or guess in corrects:
        print("You have already guessed this letter before.")
        return

    #Checking if the letter is in the word or not. Then placing it where it belongs
    if secret.count(guess) == 0:
        misses.append(guess)
        return
    for letter in range(len(secret)):
        if secret[letter] == guess:
            displayHolding[letter] = guess
    corrects.append(guess)

    #Displaying the amount of times the letter is in the secret word
    if secret.count(guess) == 1:
        print("There is 1 instance of " + guess + " in the secret word.")
    else:
        print("There are {} instances of {} in the secret word.".format(secret.count(guess), guess))
    return


def gameContinuation(userInput):
    global ourWords
    global secretWord
    global displayWord
    global missedGuesses
    global correctGuesses

    missedGuesses = []
    correctGuesses = []
    ourWords.remove(secretWord)

    if not ourWords: #Checking if all words have been played with and the available words is empty
        print("\nYou have beat HANGMAN! There are no more words for you to guess.")
        return False
    elif userInput == "n":
        print()
        return False

    secretWord = rd.choice(ourWords)
    displayWord = []
    for space in range(len(secretWord)):
        displayWord.append("_")

    return True


def main():
    global ourWords
    global secretWord
    global displayWord
    global missedGuesses
    global correctGuesses

    fileTxt = readFile(WORDPATH)
    addWords = fileTxt.split(", ")
    ourWords = WORDLIST
    for word in addWords:
        ourWords.append(word)

    secretWord = rd.choice(ourWords)
    displayWord = []
    for space in range(len(secretWord)):
        displayWord.append("_")
    missedGuesses = []
    correctGuesses = []
    playing = True

    print('Welcome to H A N G M A N')

    while playing:
        print()
        print("The word so far is: " + "".join(displayWord))
        display(missedGuesses, correctGuesses)
        userInput = input("Enter your guess: ").lower()
        print()
        handleUserGuess(userInput, secretWord, displayWord, missedGuesses, correctGuesses)

        if "".join(displayWord) == secretWord:
            print("Congratulations! You guessed the word correctly, the word was:", secretWord)
            userContinue = input("Would you like to keep playing?(y/n) ")
            playing = gameContinuation(userContinue)
        elif len(missedGuesses) == GUESSLIMIT:
            print("You lost! The secret word was:", secretWord)
            userContinue = input("Would you like to keep playing?(y/n) ")
            playing = gameContinuation(userContinue)

    print("Thank you for playing!")
    #Here I will add a file read for player txt to save player stats

if __name__ == "__main__":
    main()

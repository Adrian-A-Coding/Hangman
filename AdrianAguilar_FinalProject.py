"""
Name: Adrian Aguilar
Date: 7/15/24
Assignment: Final Project
Last Updated:8/7/24
Planned Improvements: Making corrections to way multiple players function as well as adding DocStrings. May need to
account which player actually won and if the guessed letters should be shared between players.
"""
from Hangman_Game import Game
import os

WORDPATH = os.path.join(os.getcwd(), "wordBank.txt")
# PLAYERPATH = os.path.join(os.getcwd(), "player.txt")
WORDLIST = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog',
            'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose',
            'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon',
            'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel',
            'whale', 'wolf', 'wombat', 'zebra']
DISPLAYIMAGES = [
    """
      (```)
     /-----\\
    /_______\\





        O
       /|\\
       \\|/
        ^
       / \\
    """,
    """
      (```)
     /-----\\
    /_______\\
        ^
        ^
        ^
        ^
        O
       /|\\
       \\|/
        ^
       / \\
    """,
    """
      (```)
     /-----\\
    /_______\\
        ^
        ^
        ^
        O
       /|\\
       \\|/
        ^
       / \\
    """,
    """
      (```)
     /-----\\
    /_______\\
        ^
        ^
        O
       /|\\
       \\|/
        ^
       / \\
    """,
    """
      (```)
     /-----\\
    /_______\\
        ^
        O
       /|\\
       \\|/
        ^
       / \\
    """,
    """
      (```)
     /-----\\
    /_______\\
        O
       /|\\
       \\|/
        ^
       / \\
    """
]  # Little guy taken by ufo


def readFile(file_path):
    if not os.path.exists(file_path):
        print('The file, ' + file_path + ' does not exist - cannot read it.')
        return ''

    file_handle = open(file_path, 'r')
    data = file_handle.read()
    file_handle.close()
    return data


def main():
    file_txt = readFile(WORDPATH)
    add_words = file_txt.split(", ")
    words = WORDLIST
    for word in add_words:
        words.append(word)

    game = Game(words)
    game.gameStartUp(False)
    # visual_state = 0
    print('\nWelcome to H A N G M A N')
    game.playGame()
    print("Game over!")


if __name__ == "__main__":
    main()

import random as rd
from Hangman_Player import Player


class Game:
    def __init__(self, word_list: list):
        self.guessLimit = 6
        self.playing = True
        self.winner = False
        self.playerList = []
        self.eliminatedPlayers = []
        self.wordChoices = word_list
        self.wordsInPlay = word_list
        self.secretWord = ""
        self.displayWord = []

    def gamePlayers(self, continuing: bool):
        if continuing:  # Continuing game, so we want to handle if players will continue or drop out
            for player in self.playerList:  # Ask each player if they want to continue playing or not
                player_input = input(player.name + " would you like to keep playing?(y/n): ").lower().strip()
                # Players who don't want to play will be removed from the playing list
                if player_input == "n":
                    self.playerList.remove(player)
                else:  # Those who stay in have their information cleaned for a new game
                    player.refreshScores(self.guessLimit, self.displayWord)
                # Checking for if all players want to quit and exit the game loop with a bool
                if not self.playerList:
                    self.playing = False
                    print("\nThank you for playing!")
                    break
        else:  # This handles the information at the start of the game in the main file to start up with fresh players
            players = 0
            while True:
                player_name = input("Enter player {}'s name: ".format(players + 1))
                if player_name == "" and players < 1:
                    print("You need to have at least one player!")
                    continue
                elif player_name == "":
                    break
                else:
                    player = Player(player_name, self.guessLimit, self.displayWord)
                    self.playerList.append(player)
                    players += 1
                    continue

    def gameStartUp(self, restart: bool):
        # If the game is just starting don't try to remove an empty secret word
        if self.secretWord != "":
            self.wordsInPlay.remove(self.secretWord)
        elif not self.wordsInPlay:  # If the players guessed all words then stop the gaming
            self.playing = False
            print("\nYou have beat HANGMAN! There are no more words for you to guess.")
        # Reset secret word to another choice, and refresh the display and make there be no current winner
        self.secretWord = rd.choice(self.wordsInPlay)
        self.displayWord = []
        for space in range(len(self.secretWord)):
            self.displayWord.append("_")
        self.winner = False
        # If all players failed then reset the playing list to the players set at the start
        if not self.playerList:
            self.playerList = self.eliminatedPlayers
            self.eliminatedPlayers = []
        self.gamePlayers(restart)  # Here we set up players if they want to continue, important to account for restarting

    def playGame(self):
        while self.playing:
            for player in self.playerList:
                print("The word so far: ", "".join(self.displayWord))
                # Below we want to check if the current player has guessed the word already using their own stored word
                if "".join(player.currentWordGuess) == self.secretWord:
                    self.winner = True
                    print("Player", player.name, "has guessed the word! The word was:", self.secretWord)
                    break
                elif player.guessesLeft == 0:  # If the player is out of guesses take them out of the player list into the eliminated list
                    print(player.name, "is out!")
                    self.eliminatedPlayers.append(player)
                    self.playerList.remove(player)
                    continue
                # Allow the player to guess and check within the player if the guess is valid and then move on
                player_guess = input("\n{} enter your guess: ".format(player.name))
                player.guessing(player_guess, self.secretWord, self.displayWord)
                player.displayScores()
            # Check if a player has won or if both players have been eliminated
            if self.winner or (not self.playerList and len(self.eliminatedPlayers) >= 1):
                print("The game has ended!")
                self.gameStartUp(True)  # Call the function knowing that the players should be restarting

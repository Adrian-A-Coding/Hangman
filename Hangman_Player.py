class Player:
    def __init__(self, given_name: str, guess_limit: int, guess_display: list):
        self.name = given_name
        self.currentWordGuess = guess_display
        self.guessesLeft = guess_limit
        self.guessedLetters = []
        self.correctLetters = 0
        self.missedLetters = 0

    def guessing(self, guess: str, secret: str, display: list):
        # Checking for any error cases in the guess
        if len(guess) > 1:
            print("\nPlease enter one letter at a time.")
            return
        elif not guess:
            print("\nPlease try again, that wasn't a letter.")
            return
        elif ord(guess) < 97 or ord(guess) > 127:
            print("\nPlease enter a letter between a-z.")
            return
        elif guess in self.guessedLetters:
            print("\nYou have already guessed this letter before.")
            return

        # Checking if the letter is in the word or not. Then placing it where it belongs
        if secret.count(guess) == 0:
            self.missedLetters += 1
            self.guessesLeft -= 1
            self.guessedLetters.append(guess)
            return
        for letter in range(len(secret)):
            if secret[letter] == guess:
                display[letter] = guess  # Will only affect the shared display word, may need to be individual only
                self.currentWordGuess[letter] = guess  # Added player's current word to match it with the secret word
        self.correctLetters += 1
        self.guessedLetters.append(guess)

        # Displaying the amount of times the letter is in the secret word
        if secret.count(guess) == 1:
            print("\nThere is 1 instance of " + guess + " in the secret word.")
        else:
            print("\nThere are {} instances of {} in the secret word.".format(secret.count(guess), guess))
        return

    def displayScores(self):  # Display the player's guesses both in letters attempted and correct/wrong
        print(self.name, "made", self.correctLetters, "correct guesses and", self.missedLetters, "wrong guesses.")
        print("Letters you've guessed so far: ", self.guessedLetters)

    def refreshScores(self, guesses: int, display: list):
        # Reset relevant variables for the player in game only relevant for new words and setting their guesses to limit
        self.guessesLeft = guesses
        self.guessedLetters = []
        self.correctLetters = 0
        self.missedLetters = 0
        self.currentWordGuess = display

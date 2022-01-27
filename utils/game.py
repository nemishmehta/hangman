import random  # Import random to choose a random word from a list of words.
import string  # Import string to create a list of all lowercase alphabets.
from typing import List  # Import List to aid in type annotations.


class Hangman():
    """
    A classic game of Hangman.
    
    ...

    Attributes
    ----------
    All attributes are pre-defined.

    Methods
    ---------
    start_game():
        Starts a game of Hangman.

    play():
        Requests a letter from the user and checks it against the chosen word.
    
    well_played():
        Informs the user that he/she has won and prints the word, number of turns taken and the total errors. It then exits the execution.

    game_over():
        Informs the user that the game is over and exits the execution.

    """
    # Possible words list can exist as a class attribute since it will remain the same for each instance created.
    possible_words: List[str] = [
        'becode', 'learning', 'mathematics', 'sessions', 'test', 'player'
    ]

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Hangman object.

        """
        # Initialized possible_words, word_to_find, correctly_guessed_letters, incorrectly_guessed letters lists as None.
        # This will avoid the lists to be appended every time a new instance is created.
        # Initialize lives, turn_count, error_count variables.
        self.word_to_find: List[str] = None
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = None
        self.wrongly_guessed_letters: List[str] = None
        self.turn_count: int = 0
        self.error_count: int = 0

    def start_game(self) -> None:
        """
        Starts a game of Hangman.

        Chooses a random word from an existing list.

        Calls play() until the game is over (either the user has guessed the word or if lives turn to 0).
        
        Calls game_over() if lives are equal to 0.
        
        Calls well_played() if all the letters are guessed.
        
        Prints the correctly and incorrectly guessed letters, lives left, count of errors and turns at the end of each turn.

        """
        # Choose a word from possible_words list using random module
        chosen_word: str = random.choice(self.possible_words)

        # Check if word_to_find and correctly_guessed_letters list are None. If yes, turn them into empty lists.
        # Append word_to_find list with characters of chosen word.
        # Append and print correctly_guessed_letters list with '_' equivalent to total number of characters of chosen word.
        for i in chosen_word:
            if self.word_to_find is None:
                self.word_to_find = []
            self.word_to_find.append(i)

            if self.correctly_guessed_letters is None:
                self.correctly_guessed_letters = []
            self.correctly_guessed_letters.append("_")
        print(self.correctly_guessed_letters)

        # Call play() method until total number of lives are equal to 0.
        # Print details of correctly and incorrectly guessed letters, lives left, count of errors and turns after each iteration.
        # Call well_played() method if all letters are guessed.
        while self.lives > 0:
            self.play(self.word_to_find)
            print(
                f"Well guessed letters: {self.correctly_guessed_letters} \n  Bad guessed letters: {self.wrongly_guessed_letters} \n Lives: {self.lives} \n Error count: {self.error_count} \n Turn count: {self.turn_count}"
            )
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()

        # Call game_over() method if lives are equal to 0.
        if self.lives == 0:
            self.game_over()

    def play(self, word: str) -> None:
        """
        Requests a letter from the user and checks it against the chosen word.

        Updates list of correctly and incorrectly guessed letters.

        Updates lives left and count of errors and turns.

        """
        # Create a list of all lowercase alphabets
        alphabet_list: List[str] = list(string.ascii_lowercase)

        # Request user to input a letter.
        # Inform user that input is not valid if it is not a lowercase alphabet.
        while True:
            letter: str = input("Please enter a letter in lowercase: ")
            if letter in alphabet_list:
                break
            print("This is not a valid input. Please try again.")

        # If letter matches one of the alphabets in the chosen word, update list of correctly_guessed_letters.
        for i, val in enumerate(word):
            if val == letter:
                self.correctly_guessed_letters[i] = letter

        # Check if wrongly_guessed_letters list is None. If yes, turn it into an empty list.
        # If letter does not match one of the alphabets in the chosen word, update list of wrongly_guessed_letters, lives and error count.
        if letter not in word:
            if self.wrongly_guessed_letters is None:
                self.wrongly_guessed_letters = []
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1

        # Update turn count after each iteration.
        self.turn_count += 1

    def well_played(self) -> None:
        """
        Informs the user that he/she has won and prints the word, number of turns taken and the total errors. 
        
        It then exits the execution.

        """
        print(
            f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors."
        )
        exit()

    def game_over(self) -> None:
        """
        Informs the user that the game is over and exits the execution.

        """
        print("Game over.")
        exit()
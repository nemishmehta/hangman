# Hangman

## Description

Hangman is a word guessing game played by two or more players where one one player thinks of a word and the other(s) try to guess it by suggesting letters within a certain number of guesses. Originally a paper and pencil game, this repository has been created replicating the game's logic in code.

## Installation

The game has been coded in Python and can be run on the terminal. Given below are a set of instructions to access and play the game:

1. Install [Python](https://realpython.com/installing-python/) (if not installed already).
2. Clone the repository to your local machine.
3. Open the terminal on your local machine and navigate to the directory in which the repo has been cloned.

## Usage

1. Type - `python main.py` to run the game.
2. If it doesn't run then try `python3 main.py`.
3. **Note**: You have five lives to guess the word. Lose them and you lose the game.
4. **Pro Tip**: The game contains a list of predefined words which can be extended if you like. Follow the steps below to do this.
 
## Update list of words

1. Use any text editor to open game.py located in utils directory.
2. Navigate it to *init* constructor method in Hangman class.
3. Find the list referenced by variable *self.possible_words*.
4. Update list with your choice of words and save the file.




## Reference
1. [Hangman - Wiki](https://en.wikipedia.org/wiki/Hangman_(game))
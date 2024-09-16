# Word Guessing Game

## Description

This project is a simple **Word Guessing Game** implemented in Python. The player attempts to guess a randomly selected word by inputting letters. The player has a limited number of attempts and loses if they fail to guess the word before running out of tries. 

## Features

- Randomly selects a word from a file (`words.txt`).
- Provides the player with 8 attempts to guess the word.
- Tracks and displays the correct guesses and missed letters.
- Ends the game when the word is fully guessed or when the player runs out of attempts.

## How to Play

1. The game will randomly select a word from a list of words found in the `words.txt` file.
2. The player will be shown a masked version of the word, where each letter is represented by a dash (`-`).
3. The player guesses letters one at a time:
    - Correct guesses are revealed in the masked word.
    - Incorrect guesses are recorded in a list of misses, and the player loses an attempt.
4. The game continues until:
    - The player successfully guesses the word (Win), or
    - The player runs out of attempts (Game Over).
5. After the game ends, the full word is displayed.

## File Structure

- `words.txt`: A text file containing a list of words, each separated by whitespace (space, tab, or newline).
- `game.py`: The Python script containing the game logic.

## Setup and Running

### Prerequisites

- Python 3.x installed on your system.

### Instructions

1. Download or clone the project repository.
2. Ensure there is a `words.txt` file in the same directory as the `game.py` file. The file should contain a list of words separated by spaces or new lines.
3. Run the game using the following command:
    ```bash
    python game.py
    ```

4. Follow the on-screen prompts to start guessing letters!

## Example Game Flow

```bash
    Word: - - - - -
  Misses: 
Attempts: 8
Guess a letter: e

    Word: - E - - E
  Misses: 
Attempts: 8
Guess a letter: x

    Word: - E - - E
  Misses: X
Attempts: 7
Guess a letter: a
```

## Future Improvements
- Add support for difficulty levels with varying numbers of attempts.
- Implement a scoring system based on remaining attempts.
- Allow the player to choose the length of the word for a more customized experience.
- Create a graphical user interface (GUI) for better user interaction.

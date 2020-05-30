import random

def load(file_name):
    with open(file_name, "r") as file_content:
        reader = file_content.read()
        word_list = reader.split()
        return word_list


def is_won(word1, word2):
    if word1 == word2:
        return True
    return False


def start():
    word_list = load("words.txt")
    word = random.choice(word_list).upper()

    attempts = 8
    misses = []
    guesses = ["-"] * len(word)

    # Gameloop
    while attempts > 0:
        print("    Word: {}".format(" ".join(guesses).upper()))
        print("  Misses: {}".format(" ".join(misses).upper()))
        print("Attempts: " + str(attempts))

        # Ask user for input and check if it is valid
        guess = input("Guess a letter: ").upper()
        if len(guess) > 1 or guess == "" or not guess.isalpha():
            print("Invalid input. Please try again...")
            continue

        if guess in word and guess not in guesses:
            for i in range(len(word)):
                if guess == word[i]:
                    guesses[i] = guess
                    
            if is_won("".join(guesses), word):
                break
        else:
            if guess not in misses:
                misses.append(guess)
                attempts -= 1
        
    if attempts > 0:
        print("YOU WON!")
    else:
        print("GAME OVER!")
    print(word)

start()
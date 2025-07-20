import random

def play_hangman():
    word_bank = {
        "PYTHON": "A popular programming language known for its simplicity",
        "KEYBOARD": "Computer input device with alphanumeric keys",
        "ELEPHANT": "Large mammal with tusks and trunk",
        "MOUNTAIN": "Natural elevation of the earth's surface",
        "GALAXY": "Massive system of stars and celestial objects"
    }
    secret_word, clue = random.choice(list(word_bank.items()))
    secret_word = secret_word.upper()
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6
    hangman_stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        ======
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ======
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ======
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ======
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |
           |
        ======
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |   /
           |
        ======
        """,
        """
           ------
           |    |
           |    O
           |   /|\
           |   / \
           |
        ======
        """
    ]
    
    print("\n=== HANGMAN GAME ===")
    print(f"CLUE: {clue}")
    print(f"The word has {len(secret_word)} letters")
    display_word = ["_"] * len(secret_word)
    print(" ".join(display_word))
    
    while wrong_guesses < max_attempts:
        guess = input("\nGuess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Correct!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print("Wrong guess!")
            wrong_guesses += 1
            print(hangman_stages[wrong_guesses])
        print(" ".join(display_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Wrong guesses left: {max_attempts - wrong_guesses}")
        if "_" not in display_word:
            print("\nCongratulations! You won!")
            return
    print(f"\nGame Over! The word was: {secret_word}")
    print(hangman_stages[6]) 
play_hangman()

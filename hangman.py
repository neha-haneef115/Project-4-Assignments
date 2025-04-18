import random

words = ["python", "hangman","elephant", "giraffe", "kangaroo", "tiger", "cheetah", "dolphin", "penguin", "rhinoceros", "ostrich", "alligator",
    "python", "developer", "function", "variable", "streamlit", "loop", "boolean", "debugging", "framework", "algorithm",
    "mountain", "volcano", "tornado", "hurricane", "earthquake", "rainforest", "sunrise", "galaxy", "asteroid", "nebula",
    "spaghetti", "sandwich", "cheesecake", "chocolate", "pancake", "blueberry", "hamburger", "pineapple", "avocado", "lasagna",
    "keyboard", "notebook", "headphones", "backpack", "sunglasses", "microscope", "umbrella", "calculator", "flashlight", "airplane",
    "pakistan", "brazil", "germany", "canada", "japan", "norway", "egypt", "france", "mexico", "thailand", "developer", "streamlit", "keyboard", "notebook", "function", "variable"]

chosen_word = random.choice(words).lower()
guessed_letters = []
tries = 6  

print("🎮 Welcome to Hangman Game!")
print("_ " * len(chosen_word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct!")
    else:
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)


    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break
else:
    print(f"Game Over! The word was: {chosen_word}")

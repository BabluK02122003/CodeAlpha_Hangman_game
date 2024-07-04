import random  
# Importing the random module for word selection
 # List of words to choose from
words = ["CodeAlpha", "Python", "Programming", "Internship", "Hangman"] 
word = random.choice(words)  
# Randomly select a word from the list
guessed_letters = ["_"] * len(word) 
# Create a list of underscores representing letters to guess
max_incorrect_guesses = 6 
# Maximum number of incorrect guesses allowed
incorrect_guesses = 0 
# Counter to track incorrect guesses

print("Welcome to Hangman!")
print("You have", max_incorrect_guesses, "chances to guess the word.")

while True:  
    print(" ".join(guessed_letters))  
    # Print the current guessed letters separated by spaces
    guess = input("Guess a letter: ").lower()  
    # Prompt the user to guess a letter, convert to lowercase

    if guess in word.lower():  
        # Check if the guessed letter is in the word (case insensitive)
        for i in range(len(word)):  
            # Iterate through the indices of the word
            if word[i].lower() == guess:
                # If the guessed letter matches the letter in the word
                guessed_letters[i] = word[i]  
                # Update the guessed_letters list at the correct index
    else:
        incorrect_guesses += 1 
        # Increment incorrect guesses counter
        print("Incorrect! You have", max_incorrect_guesses - incorrect_guesses, "chances left.")

    if "_" not in guessed_letters: 
        # If there are no more underscores in guessed_letters (word is guessed)
        print("Congratulations! You won!")
        break  # Exit the loop, game is won
    elif incorrect_guesses == max_incorrect_guesses: 
        # If maximum incorrect guesses reached
        print("Sorry, you lost. The word was", word)  
        # Print the losing message and reveal the word
        break  
        # Exit the loop, game is lost

import random

words = ["stop", "can", "there", "be", "titans", "geometry", "vikings", "commanders", "eagles", "raiders"]

word = random.choice(words)
display = ["_" for _ in word]
lives = 10  # Initialize lives once before the game starts
game_on = True

while game_on:
    guess = input("Guess a letter: ").lower()
    
    if guess in word:
        print("Correct!")
        # Update display for every occurrence of the guessed letter in the word
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"You lost a life. You have {lives} lives left.")
    
    print(" ".join(display))
    
    # Check if the player has won (no underscores left)
    if "_" not in display:
        print("Congratulations, you win!")
        game_on = False
    # Check if the player has run out of lives
    elif lives <= 0:
        print("Game over! Better luck next time.")
        game_on = False

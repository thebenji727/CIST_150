
import random # Imports the random function so that the program can use a random number to determine the word being used
from hangman_ascii import stages, logo # grabs the logo and stages ascii art from the hangman_ascii file
print(logo)
#from words import words ## This WOULD import the words from the word file, but I wanna use my own list of words for this project, if you want the words list to be used, comment out next line and uncomment this one
words = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
chosen_word = random.choice(words).lower() # tells program to choose a random word from the list
len_chosen_word = len(chosen_word) #give length of said word
#print(chosen_word) ## WOULD print the chosen word
word_display = [] # Empty list
for _ in range(len_chosen_word): #  will append a "_" to the list for the length of the chosen word
    word_display.append(('_'))
print(word_display)


lives_left = 7
game_over = False #Starting conditions of the game, program with edit and check these conditions later
bad_guess = [] # stores wrongly chosen letters
while not game_over:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in word_display or guess_letter in bad_guess: #this if is for the condition of the letter already being guessed
        print(f"You have already guessed '{guess_letter}'. Try again.")
        print(f"Number of lives left: {lives_left}")

    elif guess_letter not in chosen_word: # This elif is for a wrong choice, will deduct lives
        print(f"You chose {guess_letter}, that's wrong. You lose one life.")
        lives_left -= 1
        print(f"Number of lives left: {lives_left}")
        bad_guess.append(guess_letter) # stores the guessed letter in that empty list so that it can be checked later
        if lives_left == 0: # checks if lives is 0 and forces a game over if true
            game_over = True
            print("Game over, no more lives left. You lose...")
            print(f"The word was: {chosen_word}")

    else: # this else statement is for choosing a correct letter
        for idx, val in enumerate(chosen_word): #Checks each index in the chosen word to see if the value/character is correct
            if val == guess_letter:
                word_display[idx] = guess_letter # will display the correct letter at the correct index points on the list
    print(word_display)
    if '_' not in word_display:
        game_over = True
        print(f"You've won the game! You had {lives_left} lives left!")
    print(stages[lives_left])
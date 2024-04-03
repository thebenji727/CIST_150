
import random
from hangman_ascii import stages, logo
print(logo)
#from words import words
words = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
chosen_word = random.choice(words).lower()
len_chosen_word = len(chosen_word)
#print(chosen_word)
word_display = []
for _ in range(len_chosen_word):
    word_display.append(('_'))
print(word_display)


lives_left = 7
game_over = False
bad_guess = []
while not game_over:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in word_display or guess_letter in bad_guess:
        print(f"You have already guessed '{guess_letter}'. Try again.")
        print(f"Number of lives left: {lives_left}")

    elif guess_letter not in chosen_word:
        print(f"You chose {guess_letter}, that's wrong. You lose one life.")
        lives_left -= 1
        print(f"Number of lives left: {lives_left}")
        bad_guess.append(guess_letter)
        if lives_left == 0:
            game_over = True
            print("Game over, no more lives left. You lose...")
            print(f"The word was: {chosen_word}")


    else:
        for idx, val in enumerate(chosen_word):
            if val == guess_letter:
                word_display[idx] = guess_letter
    print(word_display)
    if '_' not in word_display:
        game_over = True
        print(f"You've won the game! You had {lives_left} lives left!")
    print(stages[lives_left])
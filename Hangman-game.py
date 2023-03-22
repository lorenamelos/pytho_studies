'''This project was part of the course '100 Days of Code: The Complete Python Pro Bootcamp for 2023'. '''

import random
import string

word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

''' - Randomly choose a word from the word_list and assign it to a variable called chosen_word.'''
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


'''- Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.'''

display = []
for _ in range(word_length):
    display += "_"

''' - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.'''

end_of_game = False
lives = 6


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
      letter = chosen_word[position]
      #print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}' )
      if letter == guess:
        display[position] = letter
       
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
      end_of_game = True
      print('You win.')
        
    print(stages[lives])



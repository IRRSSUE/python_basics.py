
#TODO: this is Hangman game

import random
word_list = ["Science", "Game", "Mars", "Cars", "girls", "education", "Computers"]

chosen_word = random.choice(word_list).lower()

display = []
for _ in range(len(chosen_word)):
  display += "_"

print(display)

ask_the_user = str(input("Please enter your guess: ")).lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == ask_the_user:
    display[position] = letter
  else:
    pass


print(display)






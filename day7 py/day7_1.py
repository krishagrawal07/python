#step1

word_list = ["ardvark", "camel", "baboon"]

#todo1 = randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)

#todo2 = ask th user to guess the letter and assign their answers to a variable called guess.Make guess lowercase

guess = input("Guess a letter: ").lower()

#todo3 = check if the letter the user guessed(guess) is one of letters in the chosen_word

for letter in chosen_word:
          if letter == guess:
                  print("Right")
          else:
                  print("Wrong")

#step2
import random
word_list = ["ardvark", "camel", "baboon"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#testing code
print(f'pssst, the solution is {chosen_word}')

#todo1 = create an empty list called display.
#for each letter in chosen_word add "_" to 'display'.
#so if the chosen word is "apple" the diplay should be ["_", "_", "_", "_", "_"] with 5 "-" representing each letter to guess

display = []
word_length = len(chosen_word)
for _ in range(word_length):
        display += "_" 
print(display)

guess = input("Guess a letter : ").lower()

#todo2 = loop through each position in the choosen_word.
#if the letter at that position matches'guess'then reveal that letter in the display at that position.
#e.g. if the user guessed "p" and the chosen word was "apple", then display should be["_", "p", "p", "_","_"].
for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
             display[position] = letter


#todo3 = print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#hint - dont't worry about getting the user to guess the next letter. we'll tackle that in step3

print(display)


                        
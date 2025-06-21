#step4

import random
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
=========
''', '''
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

end_of_game = False
word_list = ["ardvark", "camel", "baboon"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#todo1 = create a variable called 'lives' to keep track of the number of the lives left.
#set 'lives' to equal 6.

lives = 6

#testing code

print(f'pssst, the solution is {chosen_word}')

#create blanks

display = []
word_length = len(chosen_word)
for _ in range(word_length):
        display += "_" 
while not end_of_game:
 guess = input("Guess a letter : ").lower()

#check guessed letter

for position in range(word_length):
        letter = chosen_word[position]
      #  print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
              display[position] = letter

#todo2 = if guess is not a letter in the chosen_word then reduce lives by 1
#if lives goes down to 0 the should stop and print "You lose"

if guess not in chosen_word:
      lives -= 1
      if lives == 0:
            end_of_game = True
            print("You lose")
      




#join all the elements in the list ands turn it into a string.

print(f"{' '.join(display)}")

#check if user has got all the letters

if "_" not in display:
      end_of_game = True
      print("You win")

#todo3 = print the ascii art from 'stages' that corresponds to the current number of 'lives' the user remaining
print(stages[lives])












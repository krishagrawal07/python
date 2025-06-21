from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
          if guess > answer:
                  print("To high")
          elif guess < answer:
                  print("To low")
          else:
                  print(f" You got it , the answer is: {answer}")

def set_difficulty():
        level = input("choose 'easy' or 'hard':")
        if level == "easy":
                turns = EASY_LEVEL_TURNS
        else:
                turns = HARD_LEVEL_TURNS
                



print("Welcome to the number guessing game")
print("I am thinking of number between 1 to 100")
answer = randint(1, 100)
print(f"pssst, the correct answer is {answer}")
turns = set_difficulty()
print(f"You have {turns} attempts remaining to make a guess")

guess = int(input("Make a guess: "))
check_answer(guess, answer)









import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? 0 for rock , 1 for paper , 2 for scissor.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer choose {computer_choice}")

if user_input== 0 and computer_choice == 2:
        print("User wins!")

elif computer_choice > user_input:
          print("Computer wins!")
elif computer_choice == user_input:
        print("Its a draw")
            






















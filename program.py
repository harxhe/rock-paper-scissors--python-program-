import random
print("Welcome to rock paper scissors.")
#taking choice from user as input 
user=int(input("Press 1 for rock, Press 2 for paper, Press 3 for scissors----"))
#printing their choice
if user==1 :
    print(""" You chose rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif user==2:
    print(""" You chose paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
elif user==3:
    print(""" You chose scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

else: print("Wrong input")

#generating the computer's choice by using random module 
computer=random.randint(1,3)

#printing computer's choice
if computer==1 :
    print(""" Computer chose rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif computer==2:
    print(""" Computer chose paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
elif computer==3:
    print(""" Computer chose scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#deciding the winner by following rules for rock paper scissors
if user==1 :
    if computer==1: print("Tie")
    elif computer==2: print("You lose!")
    elif computer==3: print("You win!")

elif user==2 :
    if computer==2: print("Tie")
    elif computer==3: print("You lose!")
    elif computer==1: print("You win!")

if user==3 :
    if computer==3: print("Tie")
    elif computer==2: print("You win!")
    elif computer==1: print("You lose!")


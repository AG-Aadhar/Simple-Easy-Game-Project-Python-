# Intro of the Game(Stone, Paper, Scissor)
print('''Play Game.... Stone, Paper, Scissor
'1' stands for Stone(s)
'2' stands for Paper(p)
'3' stands for Scissor(sc)
''')

# Using random module
import random

# Below function is use to find out all possibilities between computer and you
def game(com,you):

    # if both computer and you choose same thing then it's a tie
    if com == you:
        return None 

    # possibilities if computer choose Stone(s)   
    elif com == "s" and you == "sc":
        return False
    elif com == "s" and you == "p":
        return True

    # possibilities if computer choose Paper(p)   
    elif com == "p" and you == "s":
        return False
    elif com == "p" and you == "sc":
        return True

    # possibilities if computer choose Scissor(sc)   
    elif com == "sc" and you == "p":
        return False
    elif com == "sc" and you == "s":
        return True

# Computer randomly choosing number
random_number=random.randint(1,3)

# if computer choose 1 then it will be equal to Stone
if random_number == 1:
    com = "s"
# if computer choose 2 then it will be equal to Paper
if random_number == 2:
    com = "p"
# if computer choose 1 then it will be equal to Scissor
if random_number == 3:
    com = "sc"

# You will enter the no.
you = int(input("Enter the no.---> "))

# if you enter 1 then it means you choose Stone
if you == 1:
    you = "s"
# if you enter 2 then it means you choose Paper
if you == 2:
    you = "p"
# if you enter 3 then it means you choose Scissor
if you == 3:
    you = "sc"

# Here function's call happen
a = game(com,you)

# This will tell what computer and you choose
print(f"computer choose {com}")
print(f"you choose {you}")

# Below are the possibilities of winning, loosing or it can be a tie
if a == True:
    print("-----> You win <-----")

if a == False:
    print('''       You loose
    ----> NOOB <----
    ''')

if a == None:
    print(" It's a Tie")
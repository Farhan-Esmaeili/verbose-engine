import random

#Papper Scissor Rock Game

game = ["Paper","Scissor","Rock"]

print("Play against computer.")
print(game)
print("Above are your choices.")
User = game[int(input("Enter index :"))]
Computer = random.choice(game)

print("Computer got :" , Computer)

if User == "Rock" and Computer == "Scissor":
    print("You won!")
elif User == "Rock" and Computer == "Paper":
    print("Computer won!")
elif User == "Scissor" and Computer == "Paper":
    print("You won!")
elif User == "Scissor" and Computer == "Rock":
    print("Computer won!")
elif User == "Paper" and Computer == "Rock":
    print("You won!")
elif User == "Paper" and Computer == "Scissor":
    print("Computer won!")
else:
    print("equaled")
import random

def roll():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  x = dice1 + dice2
  print ("Your dice are " + str(dice1) + " and " + str(dice2) + "!")
  
  if x == 6 or x == 7 or x == 8:
    return "You Win!"
  else:
    return "You Lost!"

print(roll())
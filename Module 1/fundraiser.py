x = int( input("How many people are attending the fundraiser? ") )

def fundraiser(x):
	return x * 5 - 50

y = int(fundraiser(x))
if y < 0:
  print ("You lost " + str(abs(y)) + " dollars!")
if y > 0:
  print ("You raised " + str(fundraiser(x)) + " dollars!")
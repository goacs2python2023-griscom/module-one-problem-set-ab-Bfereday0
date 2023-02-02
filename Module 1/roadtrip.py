dist = int( input("How far did you travel? (in miles) ") )
gas = int( input("What is the fuel efficiency of the car?(in miles per gallon) ") )
gasprice = int( input("What is the gas price per gallon? ") )

def roadtrip(dist, gas, gasprice):
	total = (dist / gas) * gasprice 
	total = round(total, 2)
	return total

print ("Your total cost of the road trip is " + str(roadtrip(dist, gas, gasprice)) + " dollars")
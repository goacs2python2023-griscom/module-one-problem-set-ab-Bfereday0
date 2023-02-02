bill = int( input("What was the cost of your bill? ") )
tip = int( input("What percent would you like to tip? ") )

def tipcalc(bill, tip):
	total = bill * (tip / 100 + 1)
	return total

print ("Your total is " + str(tipcalc(bill, tip)) + " dollars")
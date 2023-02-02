def mortgagecalculator():
  loan = int(input("How much money did you borrow? "))
  interest = int(input("What is the annual interest rate? "))
  interest = interest / 100
  years = 30
  x = years*12
  interestmonthly = interest/12
  y = interestmonthly*((1+interestmonthly)**x)
  z = (1+interestmonthly)**x-1
  payment = float(loan*y/z)
  payment = round(payment, 2)
  return payment
  
print("You will pay " + str(mortgagecalculator()) + " dollars every month.")
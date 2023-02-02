import math

x = int(input("How many students are there? "))

def schoolbus(x):
  busses = x / 52
  busses = math.ceil(busses)
  return busses

print(str(schoolbus(x)) + " school busses are required")
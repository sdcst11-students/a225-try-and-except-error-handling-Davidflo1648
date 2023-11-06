#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0 
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def solve_quadratic(a, b, c):
  d = b**2 - 4*a*c
  if d < 0:
    print("There are no real roots to the equation")
  elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    x = round(x, 2)
    print(f"There is one solution: {x}")
  else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    print(f"There are two solutions: {x1} and {x2}")

while True:
  while True:
    a = input("Enter the coefficient a: ")
    b = input("Enter the coefficient b: ")
    c = input("Enter the coefficient c: ")
    if is_number(a) and is_number(b) and is_number(c):
      a = float(a)
      b = float(b)
      c = float(c)
      break
    else:
      print("Those are not valid values for a, b, or c")
  solve_quadratic(a, b, c)
  answer = input("Do you want to try another equation? (y/n) ")
  if answer.lower() == "n":
    print("Goodbye!")
    break

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")

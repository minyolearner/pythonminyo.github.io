# CS50W

import sys

try: 
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print("Input a number")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot Divided By Zero") 
    sys.exit(1)

print(f"X / Y = {result}")
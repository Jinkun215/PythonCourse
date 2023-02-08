import random
import sys


try:
    upper_limit = int(input("Enter upper limit in int: "))
    lower_limit = int(input("Enter lower limit in int: "))
except ValueError:
    print("please enter in int.")
    sys.exit()

if (lower_limit > upper_limit):
    print("lower limit is higher than upper limit.")
    sys.exit()

number = random.randint(lower_limit, upper_limit)
print(number)

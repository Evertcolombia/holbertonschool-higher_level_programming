#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    if (number % 10) > 5:
        print("Last digit of {} is {} and  is\
 greather than 5".format(number, number % 10))
    else:
        print("Last digit of {} is {} and  is\
 less than 6 and not 0".format(number, number % 10))
elif number < 0:
    number = number * -1
    if (number % 10) != 0:
        print("Last digit of -{} is -{} and is\
 less than 6 and not 0".format(number, number % 10))
    else:
        print("Last digit of -{} is {} and is\
 0".format(number, number % 10))
else:
    print("La st digit of {} is {} and is\
 0".format(number, number % 10))
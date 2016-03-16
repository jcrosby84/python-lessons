#!/usr/bin/python
# Write a fizz buzz program in python.
#divisible by 3 fizz by 5 is buzz both is fizzbuzz

import sys

usernum1 = int(sys.argv[1])
usernum2 = int(sys.argv[2])

while usernum1 <= usernum2:
	if usernum1 % 3 == 0 and usernum1 % 5 == 0:
		print("Fizz Buzz")
	elif usernum1 % 3 == 0:
		print("fizz")
	elif usernum1 % 5 == 0:
		print("buzz")
	else:
		print(usernum1)
	usernum1 = usernum1 + 1


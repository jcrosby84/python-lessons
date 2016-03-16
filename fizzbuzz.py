#!/usr/bin/python
# Write a fizz buzz program in python.

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

while start < end:
    if start % 3 == 0 and start % 5 == 0:
        print "FizzBuzz"
    elif start % 3 == 0:
        print "Fizz"
    elif start % 5 == 0:
        print "Buzz"
    else:
        print start
    start += 1

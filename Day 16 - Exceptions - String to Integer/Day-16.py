#!/bin/python3

import sys

try:
    number = int(input())

except ValueError:
    print("Bad String")
    sys.exit()
print(number)

#S = input().strip()
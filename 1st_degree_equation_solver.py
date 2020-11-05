#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Values
a = 0
b = 0
x = 0
c = 0

# Ask the user for values

a = float(input("Write a number for a value: ").replace(".", ","))
b = float(input("Write a number for b value: ").replace(".", ","))
c = float(input("Write a number for c value: ").replace(".", ","))

print("The equation to solve is: {} * x + {} = {}".format(a,b,c))

if a != float(0):
    x = (c-b)/a
    print("The result of the operation is: {}".format(x))
else:
    print("It cannot be divided by 0! Choose another number: ")


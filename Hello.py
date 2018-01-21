#!/usr/bin/env python3
# Author: Kyleigh
# Date: 1/14/2018

def get_stuff():
  name = input("What is your name? ")
  age = int(input("How old are you? "))
  return name, age
    
def print_stuff(name, age):
  print("Nice to meet you, " + name + "!")
  if age > 50:
    print("You're too old!")
  else:
    print("You're too young!")

stuff = get_stuff()
print_stuff(stuff[0], stuff[1])

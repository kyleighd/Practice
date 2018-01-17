#!/bin/env python3
<<<<<<< HEAD
# Author: Kyleigh
# Date: 1/14/2018

def get_name():
  return input("What is your name? ")

def get_age():
  return int(input("How old are you? "))
  
def print_stuff(name, age):
  print("Nice to meet you, " + name + "!")
  if age > 50:
    print("You're too old!")
  else:
    print("You're too young!")
    
name = get_name()  
age = get_age()
print_stuff(name, age)


=======

name = input("Hi, what's your name? ")
print("Nice to meet you, " + name + "!")

age = int(input("How old are you? "))
if age > 50:
  print("You're too old! ")
else:
  print("You're too young! ")
>>>>>>> 4e1eb890b617a1cccf49b4123b8e293363a40dd8

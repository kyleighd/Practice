#!/usr/bin/env ruby
# Author: Kyleigh
# Date: 1/21/2018

def get_stuff()
  print("What is your name? ")
  name = gets.chomp
  print("How old are you? ")
  age = gets.chomp.to_i
  return name, age
end

def print_stuff(name, age)
  puts ("Nice to meet you, #{name}!")
  if age > 50
    puts ("You're too old!")
  else
    puts ("You're too young!")
  end
end

stuff = get_stuff()
print_stuff(stuff[0], stuff[1])

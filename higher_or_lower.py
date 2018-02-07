#!/usr/bin/env python
# Author: Kyleigh
# Date: 2/1/2018


import random

guesses = None
secret = None
game_on = None

def difficulty_level_easy():
  global secret
  global game_on
  secret = int(random.randrange(0,100))
  while game_on == True:
    guess = int(raw_input('Try to guess the number I give you! '))
    if guess > secret:
      print('Your guess is too high! Try guessing a little lower?')
    elif guess < secret:
      print('Your guess is a little too low, I dont think you will be beating me any time soon.')
    elif guess == secret:
      print('How did you win?! You had to of cheated.. Fine! Heres your cookie!')
      break

def start_game():
  global game_on
  game_on = True
  while 1:
    level = raw_input('Welcome to higher or lower! Please type easy, hard, or quit. ')
    level = level.lower()
    if level == 'easy':
      difficulty_level_easy()
      print('I will try to make it easier for you, but im sure you still cant beat me..')
    elif level == 'hard':
      difficulty_level_hard()
      print('You will never be able to beat me in hard mode!')
    elif level == 'quit':
      game_on = False
      print('We can play later though, right?')
      exit()
    else:
      continue

def difficulty_level_hard():
  global secret
  global guesses
  guesses = 10
  secret = int(random.randrange(0,100))
  i = 9
  for i in range(guesses):
    guess = int(input('Try to guess the number I give you! '))
    if i == 9:
      print('Hah! You guessed too many times, looks like you will never beat me..')
    elif guess > secret:
      print('You guessed too high! Try a little lower?')
    elif guess < secret:
      print('You guessed too lowww! Not even close to beating me..')
    elif guess == secret:
      print('Aww.. you won, alright. Heres your cookie..')

start_game()

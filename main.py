# Braden Leach
# OCT 23rd 2024
# Fortune Teller 

import random
import sys
import time

#load fortuens
fortunes = ['You are a winner!','A secret admirer will soon send you a sign of affection!','The one you love is much closer then you think!','Good things will happen to you by the end of the day today!','Fame and fortune will ne yours if you take the time to learn Python!','I\'m just a computer program, and have no magical powers!']

magic_colors = ['blue','red','green','yellow']

#get username
user_name = input('Please enter your first name: ')

#welcome message 
print(f'Welcome to my Python Fortune Teller program, {user_name}')

#ask if user wants a fortune
question = input('Do you want me to tell your fortune? [y/n]\n').lower

    #If else statment
if question == 'y' or 'yes':
    time.sleep(1)
    color = input('Okay! To get your fortune, please input a magic color: [blue/red/green/yellow]\n').lower
    time.sleep(1)
    print('Getting your fortune...')
    time.sleep(2)
    print(f'Here is your fortune, {user_name}')
    time.sleep(1)

    #Nested
    if color in magic_colors:
        index = random.randrange(0,5)
        print(fortunes[index])
    else:
        print('Please choose a magic color of either blue, red, green or yellow.')
        time.sleep(1)
        print('Once you have input a magic color, I will reveal your Fortune!')
else:
    print(f'Thank you for playing my Fortune Teller game today, {user_name}!')
    print('Goodbye!')


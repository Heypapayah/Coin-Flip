import random, time, math, sys, os

while True:
    print('Welcome to coin flip!')
    print('')

    t = 'y'

    while t == 'y':
        HT = ['heads', 'tails']
        R = random.choice(HT)
        
        print('The result is...')
        time.sleep(2)
        print(R)
        print('')
        break

    t = input('flip the coin again? (y/n) ')
    if t == 'n':
        print('Ok bye!')
        break


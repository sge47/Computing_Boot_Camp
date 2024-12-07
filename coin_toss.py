import random
import logging

logging.disable(logging.CRITICAL) # uncomment to disable logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
   print('Guess the coin toss! Enter heads or tails: ')
   guess = input().lower()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss_str = 'heads' if toss == 1 else 'tails'
logging.debug(f'Toss result: {toss_str} (0 for tails, 1 for heads)')

if toss_str == guess:
    print('You got it!')
else:
    print('Nope! Guess again:')
    
    # Ask for a second guess
    second_guess = input().lower()
    assert second_guess != guess, "Second guess should be different from first guess"

    while guess not in ('heads', 'tails'):
        print('Invalid input. Please enter heads or tails:')
        second_guess = input().lower()
    
    if toss_str == second_guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        
logging.debug('End of program')
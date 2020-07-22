import random
def game(hand, rating, options = ['rock', 'paper', 'scissors']):
    comp = random.choice(options)
    index_hand = options.index(hand)
    options_new = options[index_hand+1:] + options[:index_hand]
    lose = options_new[:int(len(options_new)/2)]
    win = options_new[int(len(options_new)/2):]
    if hand == comp:
        print(f'There is a draw: {hand}')
        rating += 50
    elif comp in win:
        print(f'Well done. Computer chose {comp} and failed')
        rating += 100
    elif comp in lose:
        print(f'Sorry, but computer chose {comp}')
    return rating
    
rating_file = open('rating.txt', 'rt')
rating = 0

name = input('Enter your name: ')
print('Hello', name)

optionss = input().split(',')
print("Okay, let's start")

for line in rating_file:
    if name in line:
        rating = int(line.strip(name + '\n'))
while True:
    hand = input()
    if hand == '!exit':
        print('Bye!')
        break
    elif hand == '!rating':
        print(f'Your rating: {rating}')
        continue
    elif len(optionss) == 1:
        if hand in ['rock', 'paper', 'scissors']:
            rating = game(hand, rating)
        else:
            print("Invalid input")
    elif len(optionss) != 1 and hand in optionss:
        rating = game(hand, rating, options = optionss)
    else:
        print('Invalid input')
    

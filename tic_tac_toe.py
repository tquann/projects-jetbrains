move = 1
ticks = [['_________'[x] for x in range(i, i+3) ] for i in range(0, 9, 3)]
win = []

def win_draw():
    winner = []
    for i in range(3):
        if len(set(ticks[i])) == 1:
            winner.append(ticks[i][0])
        for x in range(3):
            if ticks[0][i] == ticks[1][i] and ticks[1][i] == ticks[2][i]:
                winner.append(ticks[1][i])
    if ticks[0][0] == ticks[1][1] and ticks[1][1] == ticks[2][2]:
        winner.append(ticks[0][0])
    if ticks[0][2] == ticks[1][1] and ticks[1][1] == ticks[2][0]:
        winner.append(ticks[1][1])
    winner = list(set([x for x in winner if x != '_']))
    if len(winner) == 1:
        win.append(winner[0])
        return 'win'
    elif len(winner) == 0:
        return 'draw'

while move in range(1, 10):
    print('------------------')
    print(f'''
    | {' '.join(ticks[0])} |
    | {' '.join(ticks[1])} |
    | {' '.join(ticks[2])} |
    ''')
    print('------------------')
    
    while True:
        x, y = input().split()
        try:
            if int(x) and int(y):
                x = int(x)
                y = int(y)
                if x in range(1, 4) and y in range(1, 4):
                    x -= 1
                    y = 3 - y
                    if ticks[y][x] != '_':
                        print("This cell is occupied! Choose another one!")
                        continue
                    else:
                        if move % 2 == 1:
                            ticks[y][x] = 'X'
                        else:
                            ticks[y][x] = 'O'
                        move += 1
                        break
                else:
                    print("Coordinates should be from 1 to 3!")
        except:
            print("You should enter numbers!")            
    
    print('---------')
    print(f'''
    | {' '.join(ticks[0])} |
    | {' '.join(ticks[1])} |
    | {' '.join(ticks[2])} |
    ''')
    print('---------')
    
    if move > 4:            
        if win_draw() == 'win':
            print(f'{win[0]} wins')
            break
        elif win_draw() == 'draw' and all(i != '_' for x in ticks for i in x):
            print('Draw')
            break

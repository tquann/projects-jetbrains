money = 550
water = 400
milk = 540
beans = 120
cups = 9

def info():
    global money, milk, beans, water, cups
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def change_quant(w = 0, m = 0, b = 0, c = 0, mo = 0):
    global money, water, milk, beans, cups
    
    water += w
    milk += m
    beans += b
    cups += c 
    money += mo 

def check(w, m, b, c):
    global water, milk, beans, cups
    if water + w < 0:
        print("Sorry, not enough water!")
        return False
    elif milk + m < 0:
        print("Sorry, not enough milk!")
        return False
    elif beans + b < 0:
        print("Sorry, not enough coffee beans!")
        return False
    elif cups + c < 0:
        print("Sorry, not enough cups!")
        return False
    else:
        print("I have enough resources, making you a coffee!")
        return True
def buy():
    ask = input("1 - espresso, 2 - latte, 3 - cappuccino")
    if ask == "1":
        if check(-250, 0, -16, -1):
            change_quant(w = -250, m = 0, b = -16, c = -1, mo = 4)
    if ask == "2":
        if check(-350, -75, -20, -1):
            change_quant(w = -350, m = -75, b = -20, c = -1, mo = 7)
    if ask == "3":
        if check(-300, -100, -12, -1):
            change_quant(w = -200, m = -100, b = -12, c = -1, mo = 6)

def fill():
    global water, milk, beans, cups, money
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    beans += int(input("Write how many grams of coffee beans do you want to add:"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:"))
    
while True:
    ask = input("action: buy, fill, take, remaining, exit")
    if ask == "buy":
        buy()
    if ask == "fill":
        fill()
    if ask == "take":
        print("I gave you $"+ str(money))
        money = 0
    if ask == "remaining":
        info()
    if ask == "exit":
        break

from random import randint
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('DROP table card;')
cur.execute('''CREATE TABLE card(
                    id INTEGER,
                    number TEXT,
                    pin TEXT,
                    balance INTEGER DEFAULT 0);''')
conn.commit()


def run():

    def generate():
        id = list('400000' + str(randint(0, 999999999)).zfill(9))
        ID = ''.join(id)
        pin = str(randint(0, 9999)).zfill(4)
        print(pin)
        for i in range(len(id)):
            if i % 2 == 0:
                id[i] = str(int(id[i]) * 2)
                if int(id[i]) > 9:
                    id[i] = str(int(id[i]) - 9)

        control_num = sum([int(x) for x in id])
        if control_num % 10 == 0:
            ID += '0'
        else:
            ID += str((10 - (control_num % 10)))

        cur.execute(f'''INSERT INTO card VALUES ({1}, {ID}, {pin}, {0})''')
        conn.commit()

    def check_luhn(num):
        nums = [int(x) for x in num[:-1]]
        for i in range(0, len(nums), 2):
            nums[i] *= 2
            if nums[i] > 9:
                nums[i] -= 9
        if (sum(nums) + int(num[-1])) % 10 == 0:
            return True
        return False
    while True:
        ask = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

        if ask == 1:
            generate()

            card_num = cur.execute("SELECT number FROM card;").fetchall()[-1][0]
            card_pin = cur.execute('SELECT pin FROM card;').fetchall()[-1][0]
            print('Your card has been created')
            print("Your card number:")
            print(card_num)
            print("Your PIN")
            print(card_pin)

        if ask == 2:
            ask_num = input("Enter your card number:")
            ask_pin = input("Enter your PIN")

            card_nums = cur.execute('SELECT number FROM card;').fetchall()

            cur.execute(f'''SELECT number, pin FROM card WHERE (number = {ask_num} AND pin = {ask_pin} )''')
            if cur.fetchone() is not None:

                print("You have successfully logged in!")
                while True:
                    a = int(input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit'))
                    if a == 1:
                        balance = cur.execute(f'''SELECT balance FROM card WHERE number = {ask_num}''').fetchone()[0]
                        print(balance)
                    if a == 2:
                        income = int(input("Enter income"))
                        cur.execute(f"""UPDATE card SET balance = balance + {income} WHERE number = "{ask_num}";""")
                        conn.commit()
                        print("Income was added")
                    if a == 3:
                        trans_num = input('Enter transfer number')
                        if not check_luhn(trans_num):
                            print("Probably you made mistake in the card number. Please try again!”")
                            continue
                        if trans_num == ask_num:
                            print("You can't transfer money to the same account!")
                            continue
                        if (trans_num,) in card_nums:
                            trans_amount = int(input('Enter transfer amount'))
                            if trans_amount < int(cur.execute(
                                    f'''SELECT balance FROM card WHERE number = {ask_num};''').fetchone()[0]):

                                cur.execute(
                                    f"""UPDATE card SET balance = balance - {trans_amount} WHERE number = {ask_num};""")
                                cur.execute(
                                    f"""UPDATE card SET balance = balance + {trans_amount} WHERE number = {trans_num};""")
                                conn.commit()
                            else:
                                print("Not enough money")
                        else:
                            print("Such a card does not exist")
                    if a == 4:
                        cur.execute(f"""DELETE FROM card WHERE number = {ask_num} """)
                        conn.commit()
                    if a == 5:
                        print("You have successfully logged out")
                        break
                    if a == 0:
                        print("Bye!")
                        return
            else:
                print('Wrong card number or PIN!')
        if ask == 0:
            print("Bye!")
            return
run()
        
        
            
    
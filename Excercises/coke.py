due= 50

while due>0:
        amount= print(f" Ammount Due: {due}")
        coin= int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
                due -= coin
        else:
               continue
if due< 0:
        change= print(f" Change Owed: {abs(due)}")
else:
        change= print(f" Change Owed: 0")
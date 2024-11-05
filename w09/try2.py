numItems = input("How many items do u want? ")
mytup = ()
mylist = []

for x in range(int(numItems)):
    item_name = input("Enter item name: ")
    item_price = input("Enter item price: ")
    myTup = (item_price, item_name)
    mylist.append(mytup)

mylist.sort()

for x in range(len(mylist)): print(mylist[x][1] + " = " + mylist[x][0])


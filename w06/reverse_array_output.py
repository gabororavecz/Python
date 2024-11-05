#Variables
list = []
counter = 1
#Loop
while counter < 6:
    number = int(input("\nPlease enter " + str(counter) + " list: "))
    list.append(number)  # add number to the list
    counter += 1

#Output
print("\nNormal: ", list)
list.reverse()
print("\nReversed: ", list)

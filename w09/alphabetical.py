list = []
counter = 1
while counter < 6:
    text = str(input("\nPlease enter " + str(counter) + " list: "))
    list.append(text)  # add number to the list
    counter += 1

list.sort()
print("\nNormal: ", list)
list.reverse()
print("\nReversed: ", list)
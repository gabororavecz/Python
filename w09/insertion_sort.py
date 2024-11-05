def insertion_sort_ascending(data):
    for i in range(1, len(data)):  # for loop for the range of the length of the parameter
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key > data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

counter = 1
thislist = []
while counter <= 5:
    data = int(input("Type a number: "))
    thislist.append(data)
    counter += 1

insertion_sort_ascending(thislist)
print("Sorted array is:")
for i in range(len(thislist)):
    print("%d" % thislist[i])

insertion_sort_descending(thislist)
print("\nDescending order is: ")
for i in range(len(thislist)):
    print("%d" % thislist[i])
#variables
n = 0
positive = 0
negative = 0
#loop
for n in range (0,5):
    num = int(input("Enter a number: "))
#statement
    if num >0:
        positive=positive+num
        n += 1
    else:
        negative = ((- num) + negative)
        n += 1
#outputs
print("\nSum of positive: {} " .format(positive))
print("Sum of negative: -{} " .format(negative))

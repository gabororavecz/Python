import random

dice = random.randint (1, 6)

throws = 1
print("Throw {}".format(throws))

while dice != 6:
    dice = random.randint(1, 6)
    throws += 1
    print("Throw {}".format(throws))

print("It took {} throws to get a 6".format(throws))
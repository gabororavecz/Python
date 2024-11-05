import random

choice = input("Enter yours side (heads or tails): ")

num = random.randint(0,1)

if num == 0:
   result = "heads"

elif num == 1:
    result = "tails"


if choice == result:
    print("Good Job! You won. The coin flipped", result)

else:
    print("You lost. The coin flipped", result)






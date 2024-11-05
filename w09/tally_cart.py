def insertion_sort_ascending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


counter = 0
results = []
c_bela = 0
c_kun = 0
c_gabor = 0
c_kiss = 0
while counter != 1:
    #Candidates
    print("\nList of candidates: ")
    print("2: Bela")
    print("3: Kun")
    print("4: Gabor")
    print("5: Kiss")
    print("1 to exit")
    user_vote = int(input("Type the code for your vote: "))
    if user_vote == 1:
        counter = 1
        exit
    elif user_vote == 2:
        c_bela += 1
        print("\n** Vote computed for Bela. **")
        print("Bela: ", c_bela, " votes.")
    elif user_vote == 3:
        c_kun += 1
        print("\n** Vote computed for Kun. **")
        print("Kun: ", c_kun, " votes.")
    elif user_vote == 4:
        c_gabor += 1
        print("\n** Vote computed for Gabor. **")
        print("Gabor: ", c_gabor, " votes.")
    elif user_vote == 5:
        c_kiss += 1
        print("\n** Vote computed for Kiss. **")
        print("Kiss: ", c_kiss, " votes.")
    else:
        print("You haven't selected a candidate, try again...")
        exit
else:
    exit

results.append(c_bela)
results.append(c_kiss)
results.append(c_kun)
results.append(c_gabor)

insertion_sort_ascending(results)
print("\nSorted array is:")
print(results)

list_of_numbers = results
max_value = list_of_numbers[0]

for element in list_of_numbers:
    if element > max_value:
        max_value = element
print("The candidate winner received: ", max_value, "votes")

if max_value == c_bela:
    print("Winner is Bela.!")
elif max_value == c_kiss:
    print("Winner is Kiss!")
elif max_value == c_kun:
    print("Winner is Kun!")
elif max_value == c_gabor:
    print("Winner is Gabor!")
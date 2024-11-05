times_table = int(input("Which times table? (-1 to finish) > "))

while times_table != -1:
    for num in range(1, 13):
        print(num, "x", times_table, "=", num * times_table, "\n")
    print("\n")
    times_table = int(input("Which times table? (-1 to finish) > "))
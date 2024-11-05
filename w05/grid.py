#prompts user to enter number of columns for the grid
number_of_columns = int(input("Type the number of columns: "))

#prompts user to enter number of rows for the grid
number_of_rows = int(input("Type the number of rows: "))

for i in range(number_of_rows):
    print(" *" * number_of_columns + " ")


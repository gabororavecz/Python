# to display stars in equilateral triangular form
num = int(input("Type the length: "))
n=num
for i in range(1, num+1):
    print(' '*n, end='') # repet space for n times
    print('* '*(i)) # repeat stars for i times
    n-=1

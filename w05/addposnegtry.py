print("(enter '0' to stop)")
count_pos=0
count_neg=0
sum_pos= 0
sum_neg= 0
num=1
while num != 0:
    num = int(input("enter value: "))
    if num > 0:
        sum_pos = sum_pos + num
        count_pos +=1
    if num < 0:
        sum_neg = sum_neg + num
        count_neg -=1


if sum == 0:
    print("no values were entered")
else:
    print('positive average: ' ,sum_pos/(count_pos))
    print('negative average: ' ,sum_neg/(count_neg))
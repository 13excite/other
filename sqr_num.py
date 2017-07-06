import sys

number = sys.stdin.read().split()
sum = 0
sum_sqr = 0
for num in number:
    sum = sum + int(num)
    sum_sqr = sum_sqr + int(num) ** 2
    if sum == 0:
        print sum_sqr
        break


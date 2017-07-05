import sys

num = sys.stdin.read().rstrip()
if len(num) != 3:
    print "Ooops, wrong"
else:
    num_list = [int(i) for i in num]
    summa = 0
    for i in num_list:
        summa = summa + int(i)
    print summa

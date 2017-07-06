import sys

num = sys.stdin.read().rstrip()
int_num = int(num)
if int_num < 0  or  int_num > 1000000:
    print "Oooppsss, wrong"
else:
    if len(num) < 2:
        print "0"
    else:
        print num[-2]

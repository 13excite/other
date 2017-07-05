# int(i) for i in input().split

import sys


while True:
    my_try = 1
    num = sys.stdin.read()
    num.replace('\n', '')
    int_num = int(num.rstrip())
    print(int_num + my_try)
    my_try = my_try + 1

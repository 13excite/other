import sys

for count in sys.stdin.read():
    int_count = int(count.rstrip())
    number = 0
    if int_count >= 10000 or number >= 10000:
        print "Ooops, number is large"
    else:
       print number // int_count

    number = count


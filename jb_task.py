import sys

num = sys.stdin.read().rstrip()
if len(num) < 2:
    print "0"
else:
    print num[-2]

import sys
def equally_divide(count, number):
    if count >= 10000 or number >= 10000:
        return "Ooops, number is large"
    else:
        return number // count

try:
    count=sys.argv[1]
    number=sys.argv[2]
    print equally_divide(int(count), int(number))
except:
    print "Incorrect input, use name count num"


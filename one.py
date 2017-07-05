import sys

num_list = sys.stdin.read().split()
print num_list
count = int(num_list[0])
number = int(num_list[1])
print type(count)
print type(number)
if count >= 10000 or number >= 10000:
    print "Oooopsss"
else:
    print number // count

#    c = int(count)
#    number = 0
#    if c >= 10000 or number >= 10000:
#        print "Ooops, number is large"
#    else:
#       print number // c

#    number = c


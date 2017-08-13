import sys
my_list = []
for num in sys.stdin.read().split():
    my_list.append(num)


def localMaxLst(lstIn):
    if len(lstIn) == 0:
        return []  # no results from empty list

    lst = []  # init -- no results yet
    m = lstIn[0]  # the first element as the maximum...
    candidate = True  # ... candidate

    for elem in lstIn[1:]:  # through elements from the second one
        if elem > m:
            m = elem  # better candidate
            candidate = True
        elif elem == m:  # if equal, local maximum was lost
            candidate = False
        elif elem < m:  # if lower then possible candidate to output
            if candidate:
                lst.append(m)
            m = elem  # start again...
            candidate = False  # being smaller it cannot be candidate

    if candidate:  # if the peak at the very end
        lst.append(m)
    return lst

for elem in set(localMaxLst(my_list)):
    print elem
    

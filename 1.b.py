def addValue(t = ()):
    l = list(t)
    while True:
        x = input("Enter the number in the tuple: ")
        if(x == 'end'):
            break
        l.append(int(x))
    return tuple(l)


def addTuples(nlist = []):
    n = int(input("Enter the number of tuples to be entered in the list: "))
    for p in range(n):
        t_n = ()
        nlist.append(addValue(t_n))
    return nlist

numberList = []
def sort_tuple(slist):
    tupleList = addTuples(slist)
    print("User defined tuple-list: ",tupleList)
    output = sorted(tupleList,key = lambda p : p[-1])
    return output
print("Sorted tuple-list",sort_tuple(numberList))
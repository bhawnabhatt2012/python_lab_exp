#define  function for bubble sort
def BubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1
    return alist

#getting input
alist=[]
while True:
    inp=input("enter the number in the list:-")
    if inp=="end":
        break
    num = int(inp)
    alist.append(num)
print(alist)


print('after bubble sorting:-')
print(BubbleSort(alist))




#define insertion_sort function
def insertionSort(alist):
   for i in range(1,len(alist)):

     currentvalue = alist[i]
     position = i

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
   return alist


print("after inserting sorting:-")

print(insertionSort(alist))

li=[]
print("enter 5 values:\n")
for i in range(5):
        li.append(int(input()))

#ii)
print("Max element: ",max(li),"\nMin element: ",min(li))

#iii)
li.append(7)
print(li)
#iv)
li.remove(7)
print(li)
#v)
print("Enter element to be searched: ")
if int(input()) in li:
    print("Element found")
else:
    print("Element not found")
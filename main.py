print("----------------------------------------------------------")
#Create List

a=[45,52,55,2336]
b=[23,'Vineet',68.6,"Maithon",9631163320]

#to print value by index
print(a[0])
print(b[4])

#to print value by negative index from back
print(a[-3])

#slicing
print(b[2:4])

print(b[:4])

print(b[2:])

#print length of list
print(len(a))

print(len(b))

#to print list of size of 100
Num=[0]*100
print(Num)

print("----------------------------------------------------------")
#to add in list
a.append(100)
print(a)

#to insert in middle
a.insert(2,500)
print(a)

#to extend the list
a.extend([45,68,23,54,36])
print(a)

#to sort the list
a.sort()
print(a)

#TO REVERSE THE LIST
a.reverse()
print(a)

#to remove the no from the list
a.remove(45)
print(a)

#to count the no of words
print(a.count(52))
print("----------------------------------------------------------")

#USING LIST AS A STACK

#create a blank list
st=[]

#insert value in list
st.append(90)
st.append(87)
st.append(78)
print(st)

#to delete last inserted value
print(st.pop())

#print new value
print(st)

st.append(45)
print(st)

print("----------------------------------------------------------")
#USING LIST AS A Queue
from collections import deque

que=deque(['vineet','rakesh','raju','Anshu'])
print(que)

#to add
que.append('Goli')
que.append('Aryan')
print(que)

#to pop a element
print(que.popleft())
print(que.popleft())
print(que)

print("----------------------------------------------------------")
list1=[12,'Vineet',89.7,'Delhi',7+8j]
print(list1)

del list1[2]
print(list1)

list1[2]='maithon'
print(list1)

print("----------------------------------------------------------")
#NESTED LIST
#to create list inside list

std=[1,'Vineet','Maithon','BTECH',[90,91,93,94,95]]
print(std)

#to see a particalur value
print(std[4])

#to see a particalur value in a specific list
print(std[4][2])

print("----------------------------------------------------------")
#MATRIX

mat1=[[1,2,3],[4,5,6],[7,8,9]]
print(mat1)

print(mat1[2])

#to print square
sq=[x**2 for x in range(10)]
print(sq)

#to print even number
sq=[2*x for x in range(11)]
print(sq)

#to print odd number
sq=[2*x+1 for x in range(11)]
print(sq)
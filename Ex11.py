Program:

numlist=[]
number=int(input("please enter the total number  of list elements :"))
for i in range(number):
	value=int(input ("please enter the value  of element :"))
	numlist.append(value)
numlist.sort()
print("Ascending order is :",numlist)
numlist.sort( reverse = True )
print("Descending order is :",numlist)

output:

please enter the total number  of list elements :4
please enter the value  of element :56
please enter the value  of element :76
please enter the value  of element :44
please enter the value  of element :2
Ascending order is : [2, 44, 56, 76]
Descending order is : [76, 56, 44, 2]

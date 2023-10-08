program:
def calcpercentgrad(s1,s2,s3,s4,s5):
	total=s1+s2+s3+s4+s5
	average=total/5.0
	percentage=total*100/500.0
	if average>=90:
		grade='A'
	elif average>=80 and average <90:
		grade='B'
	elif average>=70 and average<80:
		grade='C'
	elif average>=60 and average<70:
		grade='D'
	else:
		grade='E'
	print("\n The total  mark of :",total)
	print("\n The average mark is :",average)
	print("\n The percentage  is :",percentage)
	print("\n The grade is :",grade)
name=input("The student name:")	
print("Enter the five subjects mark")
sub1=float(input("sub1:"))	
sub2=float(input("sub2:"))
sub3=float(input("sub3:"))
sub4=float(input("sub4:"))
sub5=float(input("sub5:"))
calcpercentgrad(sub1,sub2,sub3,sub4,sub5)

output:
The student name:The student name:The student name:
Enter the five subjects mark
sub1:89
sub2:66
sub3:74
sub4:87
sub5:90

 The total  mark of : 406.0

 The average mark is : 81.2

 The percentage  is : 81.2

 The grade is : B

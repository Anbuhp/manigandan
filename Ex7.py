Program:
def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1 )
num=int(input("Enter a number : "))
print("The factorial of a {0} is ".
format(num),factorial(num))

output:

Enter a number : 5
The factorial of a 5 is  120

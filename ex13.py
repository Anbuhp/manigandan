fname = input("Enter the name of the file:") 
infile = open(fname, 'r') 
lines = 0 
words = 0 
characters = 0 
for line in infile: 
    wordslist = line.split() 
    lines = lines + 1 
    words = words + len(wordslist) 
    characters = characters + len(line) 
print("No of Lines:",lines) 
print("No of Words:",words) 
print("No of Characters:",characters)
output:
Enter the name of the file:simple.py
No of Lines: 2
No of Words: 5
No of Characters: 48


Lab:13

Program:

name = input('Enter Name of Employee :')
Post = input("Enter Employee Post : ")
basic_salary=int(input("Enter the Basic salary:"))
da=0.4*basic_salary;
hra=0.2*basic_salary;
gross_salary=basic_salary+da+hra;
print("DA = ",da)
print("HRA = ",hra)
print("Gross Salary = ",gross_salary)
Output:
Enter Name of Employee :Shakthivel
Enter Employee Post : Teacher
Enter the Basic salary:20000
DA =  8000.0
HRA =  4000.0
Gross Salary =  32000.0

Lab:13

Program:
num=int(input("Enter the number of employee:"))
count=1
employee=dict()
while count <=num:
    name=input("Enter the name of the Employee :")
    post=input("Enter Employee post :")
    salary=int(input("Enter the salary :"))
    employee[name]=post,salary
    count+=1
print("\n\n EMP_NAME POST  \tSALARY ")
for k in employee:
    print(k,"\t",employee[k])

output:
Enter the number of employee:2
Enter the name of the Employee :Anbu
Enter Employee post :Web Developer
Enter the salary :30000
Enter the name of the Employee :Mani
Enter Employee post :Editer
Enter the salary :35000


 EMP_NAME POST  	SALARY 
Anbu 	 ('Web Developer', 30000)
Mani 	 ('Editer', 35000)

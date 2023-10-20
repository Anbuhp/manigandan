ex.no:14
program:

student={}
print("Enter student details")
while True:
    roll_number=int(input("Enter 6 digit roll no:"))
    if roll_number in student:
        print("Roll number already exist")
    else:
        name=input("Enter name:")
        student[roll_number]=name
        print("Record added")
    ans=input("Do you want to continue (y/n):")
    if ans in "nN":
        break
    print("\n Roll Number","\t name")
    for roll_number in student:
        print(roll_number,"\t\t",student[roll_number])
    #creating a new record
        print("\n Enter a new record")
    roll_number=int(input("Enter your 6 digit roll number:"))
    if roll_number in student:
        print("Roll number alreay exists")
    else:
        name=input("enter name:")
        student[roll_number]=name
        print(roll_number,"\t\t",student[roll_number])
        #deleting a record
    print("\n Delete a record ")

    roll_number=int(input("Enter roll number:"))
    if roll_number in student:
        del student[roll_number]
        print("Record deleted")
    else:
        print("record not found")
    #modifying a record
    print("\n Modify a record")
    roll_number=int(input("Enter your 6 digit roll number:"))
    if roll_number in student:
        name=input("Modify name:")
        student[roll_number]=name
        print("record updated")
    else:
        print("record not found")
              
 output:
  Enter student details
Enter 6 digit roll no:172733
Enter name:Anbu
Record added
Do you want to continue (y/n):y

 Roll Number 	 name
172733 		 Anbu

 Enter a new record
Enter your 6 digit roll number:172734
Enter name:Mani.E
172734 		 Mani.E

 Delete a record
Enter roll number:172735
Record not found

 Modify a record
Enter your 6 digit roll number:172733
Modify name:Anbu.E
Record updated
Enter 6 digit roll no:172734
Roll number already exist
Do you want to continue (y/n):n                

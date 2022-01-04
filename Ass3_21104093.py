#taking inputs of student's SID,Name,Gender,Course name and CGPA
SID=int(input("Enter your SID:",))
Name=str(input("Enter your name:",))
Gender=str(input("Enter your gender(M for male,F for female and U for unknown):",))
Course_name=str(input("Enter your couse name:",))
CGPA=float(input("Enter your CGPA:",))
#making a list of these inputs
Student=[SID,Name,Gender,Course_name,CGPA]
print(Student)

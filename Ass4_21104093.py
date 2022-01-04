#taking input of five students's marks
first_number=int(input("Enter numbers of first student:",))
second_number=int(input("Enter numbers of second student:",))
third_number=int(input("Enter numbers of third student:",))
fourth_number=int(input("Enter numbers of fourth student:",))
fifth_number=int(input("Enter numbers of fifth student:",))
#making a list of the marks
list_marks=[first_number,second_number,third_number,fourth_number,fifth_number]
print("Before sorting:",list_marks)
#sorting list
list_marks.sort()
print("After sorting:",list_marks)

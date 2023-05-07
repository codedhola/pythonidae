student_height = input("Please enter list of student height: ").split()

total_height = 0
average_height = int
for height in student_height: 
    total_height += int(height)
    average_height = round(total_height / len(student_height), 4)
# print(student_height)
# print(total_height)
print(average_height)


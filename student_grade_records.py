# Create tuples containing information on students

student1 = ("Alice Johnson", 12345, 85, 92, 78)
student2 = ("Bob Smith", 54321, 78, 85, 88)
student3 = ("Carol Davis", 32145, 95, 89, 91)

# Access and print the name and student ID of each student using indexing.

print(f"Name: {student1[0]}, ID: {student1[1]}")
print(f"Name: {student2[0]}, ID: {student2[1]}")
print(f"Name: {student3[0]}, ID: {student3[1]}")

# Calculate and print the average test score for student1 by accessing the score elements. (Don't use functions, just do the calculation directly)

student1_average_score = sum(student1[2::]) / len(student1[2:])
print(f"Average score of {student1[0]}: {student1_average_score:.2f}")

student2_average_score = sum(student2[2::]) / len(student2[2:])
print(f"Average score of {student2[0]}: {student2_average_score:.2f}")

student3_average_score = sum(student3[2::]) / len(student3[2:])
print(f"Average score of {student3[0]}: {student3_average_score:.2f}")

# Create a tuple called all_students that contains all three student tuples (nested tuple)

all_students = (student1, student2, student3)

print(all_students)

# Use tuple unpacking to extract the name and ID from student2 into separate variables, then print them.

student2_name, student2_id, *student2_scores = all_students[1]

print(f"Student2 name is: {student2_name}, student2's id is: {student2_id}")

# Create a new tuple called student1_updated with the first test score changed to 100 (create a new tuple with the modified value).

student1_updated = ("Alice Johnson", 12345, 100, 92, 78)

# Print the total number of students using len() on all_students.

num_students = len(all_students)
print(f"Total number of students is {num_students}")

# Check if student ID 12345 exists in student1 using the in operator.

# check if it exists in the tuple student1

if 12345 in student1:
    print(True)

# chek if id is 12345

if student1[1] == 12345:
    print(True)

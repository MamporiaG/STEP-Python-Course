# create sets containing courses

student1_courses = {"MATH101", "ENG202", "PHYS150", "HIST110"}
student2_courses = {"ART303", "LAW400", "MATH101", "GEO707"}
student3_courses = {"LAW400", "GER207", "ENG202", "ESP901"}

# Print all three sets and observe how the order might differ from how you entered them.

# sets are unordered, each time will be printed with different order

print(student1_courses)
print(student2_courses)
print(student3_courses)

# Try to add a duplicate course to student1_courses (a course already in the set).
# Print the set and observe what happens. Write a comment explaining why.

# sets do not take duplicates

student1_courses.add("ENG202")
print(student1_courses)

# Remove one course from student2_courses using the remove() method.

student2_courses.remove("LAW400")
print(student2_courses)

# Add a new course to student3_courses using the add() method.

student3_courses.add("HIST110")
print(student3_courses)

# Find and print the courses that both student1_courses and student2_courses have in common (intersection).

intersection = (
    student1_courses & student2_courses
)  # or second option: intersection = student1_courses.intersection(student2_courses)

print(intersection)


# Find and print all unique courses taken by either student1_courses or student2_courses (union).

unique_course = student1_courses | student2_courses
print(unique_course)

# Find and print courses that student1_courses has but student2_courses doesn't (difference).

student1_courses_diff = (
    student1_courses - student2_courses
)  # or student1_courses_diff = student1_courses.difference(student2_courses)
print(student1_courses_diff)


# Check if "MATH101" is in student1_courses using the in operator.
print("MATH101" in student1_courses)


# Create a set of all available courses called all_available_courses with at least 8 courses.

all_available_courses = student1_courses | student2_courses | student3_courses
print(all_available_courses)

# Check if student1_courses is a subset of all_available_courses.

print(student1_courses.issubset(all_available_courses))

# Print the total number of courses in student2_courses using len().

num_student2_courses = len(student2_courses)
print(num_student2_courses)

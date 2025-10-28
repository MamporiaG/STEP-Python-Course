# Initialize student data

students = {
    "student1": {
        "name": "Alice Johnson",
        "age": 20,
        "email": "alice@school.edu",
        "grades": {"Math": 85, "Science": 92, "English": 78},
    },
    "student2": {
        "name": "Bob Smith",
        "age": 22,
        "email": "bob@school.edu",
        "grades": {"Math": 78, "Science": 85, "English": 88},
    },
    "student3": {
        "name": "Carol Davis",
        "age": 21,
        "email": "carol@school.edu",
        "grades": {"Math": 95, "Science": 89, "English": 91},
    },
}

# Update student information

students["student3"]["grades"].update({"History": 82})

# print the student data and calculate and print the average points
averages = {}

for (
    student_id,
    student_info,
) in (
    students.items()
):  # for key, value in dictionary / .items() = keys & values / loop student1, then student 2 and 3
    print(f"\n{student_id.upper()}")  # print STUDENT1, STUDENT2, STUDENT2
    print(f" Name: {student_info["name"]}")  # print names
    print(f" Age: {student_info["age"]}")  # print ages
    print(f" Email: {student_info["email"]}\n")  # print emails

    grades = student_info["grades"]
    total_points = sum(
        grades.values()
    )  # grades.values() = total values stored in grades

    for subject, points in grades.items():  # for key, value in grades
        print(
            f"\t{subject}: {points}"
        )  # prints first subjects (math, science, english) then points

    average_point = total_points / len(
        grades
    )  # sum of values in grades divided by the number of elements in grades
    averages[student_info["name"]] = (
        average_point  # averages["Alice"] = average_point / averages = {"Alice": 87.67 }
    )

    print(f"\tAverage: {average_point:.2f}\n")

# calculate average points for each student

# find max value (highest average score) in a dictionary of averages{}

top_performer = max(
    averages, key=averages.get
)  # averages{} after for loop stored names and average points

# max(averages) returns largest key itself (alphabetically),
# max(averages, key=averages.get), returns key which has largest value assigned / checks value (points) for comparison

print(
    f"The top performer is {top_performer} with average grade {averages[top_performer]}\n"
)

# calculate subject averages of the class

# creating list for each subject and storing elements in the lists

math = []
science = []
english = []

# looping through dictionaries (starts with student1, then 2 and 3)

for student in students.values():
    math.append(student["grades"]["Math"])
    science.append(student["grades"]["Science"])
    english.append(student["grades"]["English"])

# calculate total for each list and then average

total_math = sum(math)
total_science = sum(science)
total_english = sum(english)

average_math = total_math / len(math)
average_science = total_science / len(science)
average_english = total_english / len(english)

print(
    f"Average Math: {average_math:.2f} \n Average Science: {average_science:.2f} \n Average English: {average_english:.2f}"
)

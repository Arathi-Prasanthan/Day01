# 📚 Mini Project – Student Marks Analyzer

# Now let's combine everything you've learned today.

# 🎯 Task

# Write a program that:

# Create a list:
# marks = [85, 90, 76, 95, 88]
# Print each mark using a for loop.
# Print the total number of marks using len().
# Print the first mark.
# Print the last mark.
# Add a new mark 100 using append().
# Print the updated list.

# marks = [85, 90, 76, 95, 88]
# for x in marks:
#     print(x)
# print("Total number of marks:",len(marks))
# print("The first mark is :",marks[0])
# print("The last mark is:",marks[-1])
# x=marks.append(100)
# print("The updated list is :",marks)

# 🏆 Mini Assignment (Day 5 Final)

# After Challenge 7, write a program that:

# Creates this list:
# subjects = ["Python", "AI", "ML", "Data Science"]
# Prints each subject using a for loop.
# Prints the total number of subjects.
# Appends "Deep Learning" to the list.
# Removes "AI" from the list.
# Prints the updated list

# subjects = ["Python", "AI", "ML", "Data Science"]
# for subject in subjects:
#     print(subject)
# print("The total number of subjects are:",len(subjects))
# subjects.append("Deep Learning")
# subjects.remove("AI")
# print("The updated list is :",subjects)

# 🎁 Homework (Optional)

# Try writing a program that:

# students = ["Arathi", "Rahul", "Priya", "John"]

# Your task:

# Print each student's name using a for loop.
# Print the total number of students.
# Add "Anjali" to the list.
# Remove "Rahul" from the list.
# Print the final list.

students = ["Arathi", "Rahul", "Priya", "John"]
for student in students:
    print(student)

print("The total number of students are",len(students))
students.insert(2,"Anjali")
students.remove("Rahul")
print("The final list is :",students)
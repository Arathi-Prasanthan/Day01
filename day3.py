# Create a Python program that:

# Takes a student's marks as input.
# Converts the input into an integer.
# If marks are 50 or above, print "Pass".
# Otherwise, print "Fail".
# 💡 Don't worry about getting the syntax perfect.

# Try to write it yourself using:

# input()
# int()
# if
# else

# marks=int(input("Enter a mark:"))
# if marks >=50:
#     print("Pass")
# else:
#     print("Fail")

# Problem: Grade Calculator

# Write a program that takes marks as input and prints:

# 90–100 → A Grade
# 75–89 → B Grade
# 50–74 → C Grade
# Below 50 → Fail

# You'll need:

# input()
# int()
# if
# elif
# else

# marks=int(input("Enter mark:"))
# if marks >=90:
#     print("A grade")
# elif marks >=75:
#     print("B grade")
# elif marks >=50:
#     print("C grade")
# else:
#     print("Fail")

# 🎯 Job Eligibility Checker

# Create a program that asks the user for:

# age
# whether they have a degree (True/False)
# years of experience

# Then use this rule:

# A candidate is eligible if they are 21 or older AND have a degree, OR they have 2 or more years of experience.

# Hint

# You'll need:

# input()
# int()
# if
# else
# and
# or
# age =int(input("enter age:"))
# has_degree =input("do you have degree(True/False):")
# experience = float(input("enter years of experience:"))
# if (age>=21 and has_degree=="True") or experience>=2:
#     print("Eligible for job")
# else:
#     print("Not eligible")

# Student Result Analyzer

# Write a program that asks the user for:

# Student name
# Marks

# Then:

# 90 or above → "Excellent"
# 75–89 → "Very Good"
# 50–74 → "Pass"
# Below 50 → "Fail"

# And additionally:

# If marks are 100 or above, print "Invalid marks".
# Example
# Enter student name: Arathi
# Enter marks: 85

# Arathi
# Very Good
# student_name=input("Enter student name:")
# marks=int(input("enter marks:"))

# print(student_name)
# if marks>=100:
#     print("Invalid marks")
# elif marks>=90:
#     print("Excellent")
# elif marks >=75:
#     print("Very good")
# elif marks>=50:
#     print("Pass")
# else:
#     print("Fail")
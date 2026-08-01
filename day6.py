# 🎯 Mini Project

# After Challenge 3, write a function that:

# Function Name: cube

# It should:

# Accept one number as a parameter.
# Return the cube of that number.
# Call the function with 3.
# Print the returned result.

# Expected Output:

# 27

# def cube(num):
#     return num*num*num
# x=cube(3)
# print(x)

# 🎯 Mini Project

# Write a function named student_details() that:

# Returns:
# "Arathi"
# 23
# "AI Engineer"
# Store the returned values in three variables.
# Print all three variables.

# def student_details():
#     return "Arathi",23,"AI Engineer"
# name,age,course=student_details()
# print(name,age,course)

# 🎯 Final Challenge (Day 6)

# Let's combine everything you've learned about functions.

# Write a program that:

# Create a function called employee_details.
# The function should accept three parameters:
# name
# company
# salary
# The function should return all three values.
# Call the function using:
# employee_details("Arathi", "UST Global", 50000)
# Store the returned values in three variables.
# Print them like this:
# Employee Name : Arathi
# Company       : UST Global
# Salary        : 50000

def employee_details(name,company,salary):
    return name,company,salary
x,y,z=employee_details("Arathi", "UST Global", 50000)
print("Employee Name:",x)
print("Company:",y)
print("Salary:",z)

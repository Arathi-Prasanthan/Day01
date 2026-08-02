# 🎯 Mini Assignment

# Write a program that:

# Creates this dictionary:
# student = {
#     "name": "Arathi",
#     "age": 23
# }
# Add a new key:
# "course": "AI Engineering"
# Update the age to 24.
# Print the complete dictionary.

# student = {
#     "name": "Arathi",
#               "age": 23
# }
# student["course"]="AI Engineering"
# student["age"]=24
# print(student)

# 🎯 Mini Assignment

# Write a program that:

# Creates this dictionary:
# employee = {
#     "name": "Arathi",
#     "company": "UST Global",
#     "salary": 50000
# }
# Remove "company" using pop().
# Remove "salary" using del.
# Print the final dictionary.

# employee = {
#      "name": "Arathi",
#     "company": "UST Global",
#     "salary": 50000
#  }
# employee.pop("company")
# del employee["salary"]
# print(employee)

# 🎯 Mini Assignment

# Write a program that:

# employee = {
#     "name": "Arathi",
#     "company": "UST Global",
#     "salary": 50000
# }

# Using a for loop with .items(), print the output like this:

# name : Arathi
# company : UST Global
# salary : 50000

# employee = {
#      "name": "Arathi",
#      "company": "UST Global",
#      "salary": 50000
#  }
# for keys ,values in employee.items():
#     print(keys ,":",values)

# Homework (Optional)

# Practice writing these programs without looking at your notes:

# Create a dictionary and print all its values.
# Add a new key and update an existing value.
# Remove one key using pop() and another using del.
# Print all keys using a for loop.
# Print all values using .values().
# Print both keys and values using .items().

# shop={
#     "apple":250,
#     "banana":370,
#     "guava":270,
#     "milk":200
# }
# shop["strawberry"]=560
# shop["milk"]=300
# shop.pop("apple")
# del shop["banana"]
# for keys in shop:
#     print(keys)

# for values in shop.values():
#     print(values)

# for key,value in shop.items():
#     print(key,":",value)
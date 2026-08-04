# 🎯 Mini Assignment

# Write a Python program that:

# Opens a file named student.txt in write mode.
# Writes your name into the file.
# Closes the file.
# Opens the same file in append mode.
# Adds a new line with:
# Learning AI
# Closes the file.

# file=open("student.txt","w")
# file.write("Arathi")
# # file=open("student.txt","r")
# # print(file.read())
# file.close()
# file=open("student.txt","a")
# file.write("\n Learning AI")
# file.close()
# file=open("student.txt","r")
# print(file.read())
# file.close()

# Tiny Homework (5 minutes)

# Without looking at today's solution, try writing a program to find the smallest number in this list:

# numbers = [12, 45, 8, 90, 32]

# numbers=[12, 45, 8, 90, 32]
# smallest=numbers[0]
# for current in numbers:
#     if current<smallest:
#         smallest=current
# print("The smallest value in the list is:",smallest)

# Challenge

# Write a program to find the sum of all numbers in this list:

# numbers = [12, 45, 8, 90, 32]

# numbers = [12, 45, 8, 90, 32]
# sum=0
# for num in numbers:
#     sum=sum+num

# print("The sum of all numbers in the list is :",sum)

# 🎯 Bonus Challenge (No Help This Time 😄)

# I want to see if you can solve this independently.

# Write a program to find the average of all numbers in the list.

# numbers = [12, 45, 8, 90, 32]

# numbers = [12, 45, 8, 90, 32]
# total=0
# for num in numbers:
#     total=total+num
# count_of_numbers=len(numbers)
# average=total/count_of_numbers
# print("The average of all numbers in the list is :",average)

# 🎯 A Small Optional Challenge

# If you have a few minutes today, think about this:

# numbers = [12, 45, 8, 90, 32]

# Can you write a program that counts:

# How many even numbers are there?
# How many odd numbers are there?

# numbers = [12, 45, 8, 90, 32]
# even_count=0
# odd_count=0
# for num in numbers:
#     if num%2==0:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1

# print("Number of even numbers:",even_count)
# print("Number of odd numbers:",odd_count)

# Homework (Optional)

# If you have 10–15 minutes, try this challenge on your own:

# Find the maximum and minimum numbers in the same program.

# Example:

# numbers = [12, 45, 8, 90, 32]

numbers=[12, 45, 8, 90, 32]
smallest=numbers[0]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print("Maximum number:",largest)
print("Minimum number:",smallest)
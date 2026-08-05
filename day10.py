# Warm-up Challenge

#  challenge was:

# numbers = [10, -5, 8, -2, 0, 15]

# Write a program to count:

# Positive numbers
# Negative numbers
# Zeroes

# numbers = [10, -5, 8, -2, 0, 15]
# positive_count=0
# negative_count =0
# zero_count=0
# if len(numbers)>0:
#     for num in numbers:
    
#       if num>0:
#         positive_count=positive_count+1
#       elif num<0:
#         negative_count=negative_count+1
#       else:
#          zero_count=zero_count+1
# else:
#     print("Cannot take the count,as the list is empty")
# print("Count of positive numbers:",positive_count)
# print("Count of negative numbers:",negative_count)
# print("Count of zeroes:",zero_count)

# 💻 Mini Assignment

# Write a program that:

# Asks the user to enter an integer.
# Uses try and except.
# If the input is valid, print:
# You entered: <number>
# If the input is invalid, print:
# Please enter a valid number.

# try:
#     number=int(input("Enter a number"))
#     print("You entered:",number)
# except ValueError:
#     print("Please enter a valid number")

# 🎯 Problem

# Find the second largest number in a list.

# Example:

# numbers = [12, 45, 8, 90, 32]

# numbers = [12, 45, 8, 90, 32]
# largest=numbers[0]
# second_largest=numbers[0]
# for num in numbers:
    
#     if num>largest:
#         second_largest=largest
#         largest=num
#     elif num>second_largest:
#         second_largest=num
    
# print("The second largest number is :",second_largest)


# Problem: Find the Second Smallest Number

# Given:

# numbers = [12, 45, 8, 90, 32]

# Expected output:

# Second smallest number: 12

# numbers = [12,45, 8, 90, 32]
# smallest=numbers[0]
# second_smallest=numbers[0]
# for current in numbers:
#     if current<smallest:
#         second_smallest=smallest
#         smallest=current
#     elif current<second_smallest:
#         second_smallest=current
# print("The second smallest number is :",second_smallest)
# print(smallest)


# Find the third largest number.
#    numbers = [12,45, 8, 90, 32]

# numbers = [12,45, 8, 90, 32]
# largest=numbers[0]
# second_largest=numbers[0]
# third_largest=numbers[0]
# for current in numbers:
#     if current>largest:
#         third_largest=second_largest
#         second_largest=largest
#         largest=current

#     elif current>second_largest:
#         third_largest=second_largest
#         second_largest=current


#     elif current>third_largest:
#         third_largest=current
# print("Third largest number is:",third_largest)

# Reverse a list without using reverse() or slicing ([::-1]).
# numbers = [12,45, 8, 90, 32]

numbers = [12,45, 8, 90, 32]
for i in range(4,-1,-1):
    print(numbers[i])

   
    

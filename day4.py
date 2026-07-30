# Try writing these programs on your own:

# Ask the user for their name and print it in:
# Uppercase
# Lowercase
# Title Case
# Ask the user for a sentence and:
# Find the index of the letter "a"
# Replace all "a" with "@"
# Ask the user for their dream company (for example, "tcs") and print it using title() so it becomes "Tcs".

# name=input("enter your name:")
# print(name.upper())
# print(name.lower())
# print(name.title())

# sentence= input("enter a sentence:")
# print(sentence.find("a"))
# print(sentence.replace("a","@"))

# company=input("enter yor dream company:")
# print(company.title())

# Mini Project 1 (Real-World Practice)

# Let's build something that combines almost everything you've learned today.

# 🎯 Student Profile Analyzer

# Write a Python program that:

# Ask the user to enter their full name.
# Remove extra spaces using strip().
# Print:
# Name in uppercase.
# Name in lowercase.
# Name in title case.
# Count how many times the letter "a" appears in the name.
# Check whether the name starts with "A".
# Check whether the name ends with "n".
# Split the name into individual words.
# Replace every "a" with "@".
# Example

# If the user enters:

#    arathi prasanthan

# Your program should produce something similar to:

# ARATHI PRASANTHAN
# arathi prasanthan
# Arathi Prasanthan
# Letter 'a' count: 5
# Starts with A: False
# Ends with n: True
# ['arathi', 'prasanthan']
# @r@thi pr@s@nth@n

# name=input("enter your full name:")
# print(name.strip())
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.count("a"))
# print(name.startswith("A"))
# print(name.endswith("n"))
# print(name.split())
# print(name.replace("a","@"))

# Bonus Challenge (Optional)

# Without using Google, can you write a program that:

# Takes the user's full name.
# Prints the total number of characters using len().
# Prints the first character.
# Prints the last character.
# Prints the name in reverse using slicing ([::-1]).

name = input("Enter your full name:")
print("Total number of characters",len(name))
print("The first character is:" ,name[0])
print("The last character is:" ,name[-1])
print("The name in reverse order is :",name[::-1])



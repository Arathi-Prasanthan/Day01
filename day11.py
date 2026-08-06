# frequency count using dictionary
# numbers=[1,2,1,3,2,1]

# numbers=[1,2,1,3,2,1]
# frequency={}

# for num in numbers:
#     if num not in frequency:
#         frequency[num]=1
#     else:
#         frequency[num]=frequency[num]+1
# for key, value in frequency.items():
#     print(key,":",value)

# Write a program to count how many times each word appears.

# Example:

# words = ["AI", "Python", "AI", "ML", "Python", "AI"]

# words = ["AI", "Python", "AI", "ML", "Python", "AI"]
# frequency={}
# for item in words:
#     if item not in frequency:
#         frequency[item]=1
#     else:
#         frequency[item]+=1
# for key,value in frequency.items():
#     print(key,":",value)

# Using this list:

# numbers = [10, 20, 30, 20, 40, 10, 50]

# Print only the unique numbers.

# numbers = [10, 20, 30, 20, 40, 10, 50]
# unique_numbers=[]
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print(unique_numbers)

# Without using count() or set(), find the element that appears the most.

# Example:

# numbers = [1, 2, 1, 3, 2, 1, 2, 2]

numbers = [1, 2, 1, 3, 2, 1, 2, 2]
frequency={}
for num in numbers:
    if num not in frequency:
        frequency[num]=1
    else:
        frequency[num]+=1
max_frequency = 0
most_frequent = None

for key, value in frequency.items():
    if value > max_frequency:
        max_frequency = value
        most_frequent = key

print("Most frequent element:", most_frequent)
print("Frequency:", max_frequency)
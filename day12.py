# Can you write a method called introduce()?

# Expected output:

# Hello, my name is Arathi and I am 23 years old.

# Try writing it yourself.

# Hint:

# def introduce(self):
#     ...

# Use both:

# self.name
# self.age

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#         print("Hello , my name is ",self.name ,"and Iam ",self.age,"years old" )
# student1=Student("Arathi",23)
# student1.introduce()

# Final Challenge of Day 12 (Mini Project)
# Create a class called BankAccount.

# It should have:

# Attributes
# account_holder
# balance
# Methods

# 1. display_balance()

# Output:

# Current Balance: 5000

# 2. deposit(amount)

# If we call:

# account.deposit(1000)

# the balance should increase by 1000.

# class BankAccount:
#     def __init__(self,account_holder,balance):
#             self.account_holder=account_holder
#             self.balance=balance
#     def display_balance(self):
#           print("Current Balance:",self.balance)
#     def deposit(self):
#           self.balance+=1000

# account1=BankAccount("Diya",4000)

# account1.deposit()
# account1.display_balance()


# 🏫 Create a Book class.
# Attributes
# title
# author
# price
# Methods
# display_details()

# Example output:

# Title : Python Basics
# Author : John
# Price : 499
# discount(amount)

# If the price is ₹500 and we call:

# book.discount(50)

# The new price should become ₹450.

# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price


#     def display_details(self):
#         print("Title:",self.title)
#         print("Author:",self.author)
#         print("Price:",self.price)

#     def discount(self,amount):
#         self.price-=amount


# book1=Book("Ikigai","Theodore",5000)
# book1.discount(50)
# book1.display_details()

# Final Mini Project (Optional)

# Let's combine everything into one project.

# Employee Management System

# Create a class:

# class Employee:
# Attributes
# name
# salary
# department
# Methods
# display_details()

# Output:

# Name : Arathi
# Salary : 50000
# Department : AI
# increment(amount)

# Increase salary.

# Example:

# emp.increment(5000)

# Salary becomes:

# 55000
# transfer(new_department)

# Example:

# emp.transfer("Software Development")

# Department changes.

class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

    def increment(self,amount):
        self.salary+=amount

    def transfer(self,new_department):
        self.department=new_department

emp=Employee("Ciara",50000,"Finance")
emp.increment(5000)
emp.transfer("IT")
emp.display_details()
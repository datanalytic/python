#!/usr/bin/env python
# coding: utf-8

# In[4]:


# To improve your control flow statement skills and to raise your awareness of some algebraic knowledge.
# Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.
# The examples of the desired output are as follows :
# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number

number = int(input("Enter a positive number to check whether it is a prime number or not?: "))
list_dividing = []
for i in range(1, number + 1):
   if number % i == 0:  # Rule to decide whether the number is prime or not!
       list_dividing.append(i) # Being prime number is met, it is accordingly added to the list.
if list_dividing == [1, number]: # When the number is divisible itself or divisible with 1,
   print(f'{number} is a prime number')
else:
   print(f'{number} is not a prime number')


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Objective: To improve your control flow statement skills and to raise your awareness of some algebraic knowledge.
# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

fibo = [1, 1]
while fibo[-1] < 55:
    fibo_next = fibo[-2] + fibo[-1]
    fibo.append(fibo_next)
print(fibo)


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:57:10 2020

@author: Vasu
"""

#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

#   Fn = Fn-1 + Fn-2
#with seed values

#   F0 = 0 and F1 = 1.

def fibonacci_number(num): #function to print fibonacci number 
    if num < 0:
        print ('Invalid input')
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_number(num-1)+fibonacci_number(num-2)
    
num = (int)(input('Enter a number :'))

print(fibonacci_number(num))  #calling a function
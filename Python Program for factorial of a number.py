# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:27:14 2020

@author: vasu

"""

#Factorial of a non-negative integer, is multiplication of all
#integers smaller than or equal to n. For example factorial of 6
#is 6*5*4*3*2*1 which is 720.

def factorial_of_a_number(num): #function 
    if num ==0:
        return 0
    elif num==0 or num == 1:
        return 1
    else:
        fact = 1
        while(num>1):
            fact*=num
            num-=1
        return fact
        
    
num=5
print('the factorial of a number is ',factorial_of_a_number(num))


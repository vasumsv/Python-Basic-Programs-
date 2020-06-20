# Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.

# The program to add two numbers, the user is first asked to enter two numbers and the input is scanned 
# using the input() function and stored in the variables number1 and number2. Then, the variables number1 
# and number2 are added using the arithmetic operator + and the result is stored in the variable sum.

num1 = (int)(input("enter the first number"))
num2 = (int)(input("enter the second number"))
sum =  num1 + num2


print('The sum of two  numbers are ',sum)

print(type(sum))





#Format 2 to print number 

print('the first number is {0} and second number is {1} and sum of both the number is {2}'.format(num1,num2,sum))
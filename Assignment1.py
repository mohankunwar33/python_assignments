print('''-------------------| Assignment-1 | QUESTIONS & ANSWERS |----------------------------''')
print()
print("Question-1")
print('''You are provided write two numbers. A and B. Your task is to add these two numbers.
      Note : you have to complete AddTwoNumbers function. No need to take any input.''')

A1 = 2
B1 = 5

AddTwoNumbers = (A1 + B1)
print(AddTwoNumbers)

print("----------------------------------------------------------------------------------------")

print("Question-2 (Pending as question not clear)")
print('''You are given two number first as A and second as B and check if both conditions
      A<B and A<B are satisfied or not with the help of operators.
      Note: You have to complete Is_Valid function. No need to take any input.''')

A2 = 5
B2 = 3
Is_Valid=0

if A2>B2 and B2<A2 :
    print(A2,B2)

print("----------------------------------------------------------------------------------------")

print("Question-3")
print('''You are given two numbers A and B. You need to do the following checks:
        1.  if both are divisible by 10 console ture.
        2.  if both are not divisible by 10 false.
        3.  if one of them only is divisible by 10 console trure.
      use operator to do this.
      Note : You have to Check function. No need to take any input.''')

A3 = 12
B3 = 20

def divisible(A3,B3):
    if A3 % 10 == 0 and B3 % 10 == 0 :
        print(True)
    elif A3 % 10 != 0 or B3 % 10 != 0 :
        print(False)
    else:
        print(True)
divisible(A3,B3)

print("----------------------------------------------------------------------------------------")


print("Question-4")
print('''You are provided a four digit number N only. Your task is to 
      print out the first digit of that number.
      You have to complete First_Digit function. No need to take any input.''')

N = 4567
def First_Digit():
    print(N // 1000)

First_Digit()

print("----------------------------------------------------------------------------------------")

print("Question-5")
print('''You are provided a four digit number N only. Your task is to print out the last digit of that number.
      Note : You have to complete Last_Digit function. No need to take any input.''')

N = 4567
def Last_Digit():
    print(N % 10)

Last_Digit()

print("----------------------------------------------------------------------------------------")

print("Question-6")
print('''You are provided with two numbers A and B where A as divisor and B as dividend. Your task is find the remainder
      Note : You have to complete Find_the_remainder function. No need to take any input.''')

A6 = 2
B6 = 9

def Find_the_remainder():
    print(B6 % A6)

Find_the_remainder()

print("----------------------------------------------------------------------------------------")

print("Question-7")
print('''You are provided with two numbers A and B your task is to multiply these two numbers.
      Note : You have to coplete Multiply_two_number function. No need to take any input.''')

A7 = 2
B7 = 5

def Multiply_two_number():
    print(A7 * B7)

Multiply_two_number()

print("----------------------------------------------------------------------------------------")

print("Question-8")
print('''Shyam has got his marks in theree subjects as A, B, C (out of 100). Write a program to
      calculate his total marks and his average.
      Note : You have to complete Sum and Average functions. No need to take any input.''')

A8 = 50
B8 = 20
C8 = 100

def total():
    return A8+B8+C8

def average():
    print(total()/ 3)

print(total())
average()

print("---------------------------------END--------------------------------------------------------")
    

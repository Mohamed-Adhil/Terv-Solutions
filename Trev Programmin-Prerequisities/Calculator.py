'''
Calculator
Jennifer is searching the calculator to calculate the money spend and earned. She could not find the calculator. Her son made her a program which helped her perform the basic calculations. Can you write a program to perform simpler operations?

Input Format : The first line contains an integer op--the operation (1-Addition,2-Subtraction,3-Multiplication,4-Division).

The second line contains two integers a and b--the operands.

Input Constraints : 1<=op<=4
1<=a,b<=10^7

Output Format : Print the result
Note:Print the integer value for the division and absolute value for subtraction.

Sample Input :

1
5 10
Sample Output :

15
'''

n = int(input())
a, b = map(int, input().split())
if n == 1:
    print(a+b)
elif n == 2:
    print(abs(a-b))
elif n == 3:
    print(a*b)
elif n == 4:
    print(a//b)

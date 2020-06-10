'''
I Hate Maths
You are a student who hates maths. But you are a programmer. There was this sum in second chapter. You are given with a number n. You have to find the sum of numbers from 1 to n. And subtract all the 2n values from the sum. You how to finish the exercise in the second chapter. Write a program to finish your maths homework.

Input Format : The first line contains an integer t, the total number of testcases.
The next t lines contain an integer n.

Input Constraints : 1<=t<=100
1<=n<=10^9

Output Format : Print t lines of integer values

Sample Input :

2
4
1000000000
Sample Output :

-4
499999998352516354
'''
t = int(input())
for i in range(t):
    n = int(input())
    s = n*(n+1)//2
    x = 1
    s1 = 0
    while x <= n:
        s1 += 2*x
        x *= 2
 print(s-s1)

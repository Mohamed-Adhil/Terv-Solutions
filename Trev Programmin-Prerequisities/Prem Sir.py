'''
Prem Sir
Prem is a staff member in a college and wants to allocate grades to his students. The students with 91-100 marks are provided with ‘A’ grade, 81-90 is given ‘B’ grade, 71-80 is given ‘C’ grade, 61-70 is given ‘D’ grade, 50-60 is given ‘E’ and below 50 is ‘F’ grade. He felt bored doing the same work so he made a program to do that. Can you make one?

Input Format : The first line contains an integer t--the number of test cases.
The next t line consists of an integer m--the mark of the student.

Input Constraints : 1<=t<=100
0<=m<=100

Output Format : Print t line of grades.

Sample Input :

2
95
20
Sample Output :

A
F
'''

for i in range(int(input())):
    n = int(input())
    if n >= 91:
        print('A')
    elif n >= 81 and n <= 90:
        print('B')
    elif n >= 71 and n <= 80:
        print('C')
    elif n >= 61 and n <= 70:
        print('D')
    elif n >= 50 and n <= 60:
        print('E')
    else:
        print('F')

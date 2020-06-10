'''
Intercalary
An Intercalary year is a year with one extra day. Can you write a program to check if a year is Intercalary or not?

Input Format : The first line of input contains an integer t--the number of test case.
Then the next t lines consist of a year.

Input Constraints : 1<=year<=10^9

Output Format : Print "Yes" if it's Intercalary, Otherwise "No"

Sample Input :

1
2019
Sample Output :

No
'''

for i in range(int(input())):
    n = int(input())
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print('Yes')
    else:
        print('No')

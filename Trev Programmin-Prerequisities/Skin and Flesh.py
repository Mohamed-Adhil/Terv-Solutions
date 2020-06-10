'''
Skin and Flesh
You are given an even number a and you have to generate a matrix of axa. Consider the border of the matrix as skin and inner part as flesh. Generate the axa pattern for skin=1 and flesh=0.

Input Format : The input contains an integer a--the dimension

Input Constraints : 2<=a<=10^5
a is an even number.

Output Format : Print the result

Sample Input :

4
Sample Output :

1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1
'''
n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('1 ', end='')
        else:
            print('0 ', end='')
    print()

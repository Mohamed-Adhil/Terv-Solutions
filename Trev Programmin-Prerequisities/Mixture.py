'''
Mixture
You are going to generate a mixture series and find the n-th term. The odd terms must follow a geometric series related to 2 and even terms must follow a geometric series related to 3.

Input Format : The input contains an integer n

Input Constraints : 1 ≤ N ≤ 100

Output Format : Print an integer

Sample Input :

16
Sample Output :

2187
'''
n = int(input())
if n % 2 == 0:
    print(int(3**((n/2)-1)))
else:
    print(int(2**((n-1)/2)))

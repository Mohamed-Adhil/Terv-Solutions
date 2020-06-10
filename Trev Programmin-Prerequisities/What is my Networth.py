'''
What is my Net Worth
The billionaire Harlon Thrombey wants to know the total value of the factories he owns (Net Worth). He owns n factories and the value of each factory is given. Help him by writing a program.

Input Format : The first line contains single integer n--the total number of factories he owns.
The second line contains n space-separated integers d1,d2,d3.....dn where di is the value of i-th factory in million dollars.

Input Constraints : 1 ≤ N ≤ 1000
1 ≤ di ≤ 1000

Output Format : Print a single integer denoting the Net Worth of Harlon Thrombey.

Sample Input :

5
45 10 55 99 7
Sample Output :

216
'''
n = int(input())
l = list(map(int, input().split()))
print(sum(l))

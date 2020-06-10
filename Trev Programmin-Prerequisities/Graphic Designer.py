'''
Graphics Designer
Franklin is a graphics designer and he uses m applications daily. He wants to keep track of the time he spends on each application. He made a program for that and measured the time spend in m apps for n days. Now he wants to know the longest working time among n days. In other words among n working days which day he spent maximum time and the amount of time of that day. He asks your help to find the maximum worked time among n days.

Input Format : The first line contains two integers n and m--the number of days worked and the number of applications used each day.

The next n lines contain m integers t1,t2,....tm where ti is the time he spends in i-th application.

Input Constraints : 1<=n,m<=100
1<=ti<=1000

Output Format : Print a single integer denoting the maximum time spend on any day.

Sample Input :

3 3
1 2 1
1 1 1
3 5 3
Sample Output :

11
'''
a, b = map(int, input().split())
l = [[int(j) for j in input().split()] for i in range(a)]
x = []
for i in l:
    x.append(sum(i))
print(max(x))

'''
Life of a Gamer
Tim is a hellbound gamer. He earns money for playing games and streaming it on youtube. There are N hours in Tim’s each day.


For example, if N=5, then all days of his life have 5 hours.


He either plays game or takes rest in each hour of the day. For N=5, Tim has h1,h2,h3,h4,h5 hours. If hi = 1, Tim plays game on that i-th hour. If hi = 0, Tim is taking Rest.


What is the maximal number of continuous hours during which Tim plays game? It is guaranteed that there is at least one resting hour in a day.

Input Format : The first line contains an integer N, the total number of hours in Tim's day.

The next line contains N integers, h1,h2,.....hn. If hi=0, then it is a resting hour and if hi=1, then it is a gaming hour.

Input Constraints : 1<=N<=10^5
0<=hi<=1

Output Format : Print the maximal number of continuous hours during which Tim plays game. Remember that you should consider that days go one after another endlessly and Tim uses the same schedule for each day.

Sample Input :

5
1 0 1 0 1
Sample Output :

2
'''
n = int(input())
l = list(map(int, input().split()))
l1 = l.copy()
l = l+l1
m = 0
c = 0
for i in l:
    if i == 1:
        c += 1
    else:
        c = 0
    if c > m:
         m = c
print(m)

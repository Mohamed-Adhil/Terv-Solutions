'''
Winderboro
A magic island Winderboro, where Arrim lives, has its own currency system. It uses banknotes of several values. But the problem is, the system is not perfect and sometimes it happens that Winderboroians cannot express a certain sum of money with any set of banknotes. Of course, they can use any number of banknotes of each value. Such sum is called unfortunate. Arrim wondered: what is the minimum unfortunate sum?

Input Format : The first line contains number n, the number of values of the banknotes used in Winderboro.

The second line contains n distinct space-separated numbers a1, a2, ..., an, the values of the banknotes.

Input Constraints : 1<=n<=1000
1<=ai<=10^6

Output Format : Print a single line — the minimum unfortunate sum. If there are no unfortunate sums, print  - 1.

Sample Input :

5
1 2 3 4 5
Sample Output :

-1
'''
n = int(input())
l = list(map(int, input().split()))
l.sort()
if l.count(1) == 1:
 print('-1')
else:
 print('1')

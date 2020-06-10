'''
Help the Oldman
Subha is a small girl and has a play kit, containing a dummy coin that looks the same like a real coin. The difference between the real coin and the dummy coin can be identified by the ‘-’ symbol in front of the numbers in the dummy coin. Subha’s grandfather mistakenly dropped some coin into that kit while she was playing. Now he wants to take out that coin. As he is very old he cannot see the numbers clearly. Can you count the coins he dropped into the kit?

Input Format : The first line contains a single integer n--the total number of coins in the box.

The second line contains n integers c1,c2,...cn where ci is the value of the i-th coin.

Input Constraints : 1<=n<=10^5
-10^7<=ci<=10^7

Output Format : Print a single integer

Sample Input :

5
-1 -2 2 -9 -73
Sample Output :

1
'''

n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
    if i > 0:
        c += 1
print(c)

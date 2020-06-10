'''
Yalini's Coin Collection
Yalini is a small girl and loves coin collection. She has a collection of coins whose value is from 1 to n (n distinct coins). She gifted her elder brother coins on his birthday. But her brother knows it took a long time for yalu to collect those coins. So her brother refused to get it from her. But she turns out to take certain coins only from the coin bag. She took out the coin which has only one digit repeated 1 or more times. Write the program to count the number of coins yalini took out from the bag.

Input Format : The first line contains an integer t, number of test cases.
Each test case consists of one line, which contains a positive integer n

Input Constraints : 1<=t<=10^4
1<=n<=10^9

Output Format : Print t integers

Sample Input :

6
18
1
9
100500
33
1000000000
Sample Output :

10
1
9
45
12
81
'''

#solution 1

t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    for j in range(1, n+1):
        j = str(j)
        l = len(j)
        if j.count(j[0]) == l:
            c = c + 1
    print(c)

#solution 2 (Efficient O(n))

t = int(input())
for i in range(t):
    n = int(input())
    l = len(str(n))
    s = int('1'*l)
    print((n//s)+(9*(l-1)))

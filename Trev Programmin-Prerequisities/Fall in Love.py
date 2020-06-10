'''
Fall in Love
Cupid is a god of attraction and affection. Cupid makes people fall in love depending on a pattern that depends on their birth date. A man’s birth date is n, then his soul mate must be the one with the birthday date m.


such that,

a*a + b = n
a + b*b = m


Now n and m are given, write a program to find the number of different pairs of a and b which satisfies the condition.

Input Format : A single line contains two space-separated integers n and m, the birth dates.

Input Constraints : 1<=n,m<=1000

Output Format : Single line output

Sample Input :

9 3
Sample Output :

1
'''
n, m = map(int, input().split())
c = 0
x = max(n, m)
for i in range(32):
    for j in range(32):
        a = i*i+j
        b = i+j*j
        if a == n and b == m:
            c += 1
print(c)

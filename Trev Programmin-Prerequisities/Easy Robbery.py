'''
Easy Robbery
Secure Vault is a lock manufacturing company, they are not doing so great. Recent crime statistics show that this company’s lock is behind most of the successful robberies. They are not making distinct keys for all locks. A lock with key number 10 can be opened with all the other 1,2,5 numbered keys. Cops asked you to write a program for finding similar keys so that people can be alerted and they can change their lock.

Input Format : The input contains a single integer n.

Input Constraints : 1<=n<=10^5

Output Format : Output a list of numbers which represents keys.

Sample Input :

320
Sample Output :

1
2
4
5
8
10
16
20
32
40
64
80
160
320
'''

n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i)

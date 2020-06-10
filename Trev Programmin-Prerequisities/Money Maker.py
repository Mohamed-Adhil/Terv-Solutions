'''
Money Maker
Money making machine has a secret feature, it can make money in all the values one wants. To unlock the feature and print money in n dollars (For example, 7$ note doesn’t exist but you can make it)  one has to give all the a to n numbers to the machine. You can directly give smaller values like 4,5 and 10 but if you need a 100,000$ note then you have to give values from a-100,000.

Input Format : The first line contains two integers a and n--the range.

Input Constraints : 1<=a<n<=10^5

Output Format : Print the integers from a to n.

Sample Input :

4 10
Sample Output :

4
5
6
7
8
9
10
'''

a, n = map(int, input().split())
for i in range(a, n+1):
    print(i)

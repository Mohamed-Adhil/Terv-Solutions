'''
Icecream Quiz
Arun is an ice cream seller. He sells only 2 flavors of icecream Chocolate and Vennila. He will give one kid a free ice cream with one quiz. He will tell the kid the total number of chocolate, n he has initially. The chocolate flavor is numbered as odd values and vanilla is numbered as even values. Initially, the n icecreams are arranged in ascending order. Now Arun will give the kid a number K. The kid has to sort Chocolate flavored icecreams first and Vanilla flavored icecreams next.


The kid has to tell the value of icecream in the kth place. Help a kid get free icecream.

Input Format : The only line of input contains integers n and k

Input Constraints : 1<=n,k<=10^12

Output Format : Single integer

Sample Input :

1 1
Sample Output :

1
'''
import math
n, k = map(int, input().split())
if k <= math.ceil(n/2):
    print(2*k-1)
else:
    k = k-math.ceil(n/2)
    print(2*k)

'''
This is my will.
Harlan Thrombey is a billionaire and he owns n factories and n sons. He wants to give one factory to each son after his death. Factory 1 to Son 1, Factory 2 to Son 2,.....Factory n to Son n. Last-minute of his life he decided to change his will. He wants to give factory number 1 to nth son and nth factory to 1st son. Help him by writing a program.

Input Format : The first line contains a single interfere n--the number of sons and factories.
The second line contains n space-separated integers d1,d2,d3.....dn denoting the value of the factories in million dollars.

Input Constraints : 1 ≤ n ≤ 1000
-1000 ≤ di ≤ 1000

Output Format : Print n space-separated integers after Harlan changed his mind.

Sample Input :

5
2 4 1 5 0
Sample Output :

0 4 1 5 2
'''
n = int(input())
a = list(map(int, input().split()))
a[0], a[n-1] = a[n-1], a[0]
for i in a:
    print(i, end=' ')

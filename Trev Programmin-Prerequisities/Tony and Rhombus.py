'''
Tony and Rhombus
Tony is a boy who likes maths. One day in his maths class his maths teacher thought about rhombus and he wanted to try finding the area of it. He chose the points randomly and started finding the area. He wants to do it without any errors. But has trouble finding the area. Help him find the Area.

Input Format : The first line contains two integers a and b--the diagonal values of the rhombus.

Input Constraints : 1<=a,b<=10^5

Output Format : Print a single integer value.

Sample Input :

2 4
Sample Output :

4

'''
a, b = map(int, input().split())
print(int(a*b/2))

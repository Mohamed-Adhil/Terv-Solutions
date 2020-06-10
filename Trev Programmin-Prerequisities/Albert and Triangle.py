'''
Albert and Triangle
Albert is a boy who likes maths. One day in his maths class his maths teacher thought about triangles and he wanted to try finding the area of it. He chose the values randomly and started finding the area. He wants to do it without any errors. But has trouble finding the area. Help him find the Area.

Input Format : The first line contains 2 integers height and base

Input Constraints : 1<=height,base<=10^5

Output Format : Print the area of triangle.
Note:Print the integer value of the area.

Sample Input :

5 6
Sample Output :

15
'''

a, b = map(int, input().split())
print(int(0.5*a*b))

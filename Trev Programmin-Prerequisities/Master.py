'''
Master
A square is considered Master square if the sum of the column numbers is strictly greater than the sum of the row numbers.

To determine if the particular square is Master Square you should do the following. Calculate the sum of all numbers on the squares that share this column (including the given square) and separately calculate the sum of all numbers on the squares that share this row (including the given square).

For instance, the purple cell is Master square, because the sum of its column numbers is 24, sum of its row numbers is 19, and 24 > 19.

Your task is to find the number of Master Squares in a given nxn numbers.

Input Format : The first line contains an integer n.

And it follows nxn matrix on the next line. Values in each row are space-separated.

Input Constraints : 1<=n<=30
All numbers on the nxn are integers from 1 to 100.

Output Format : Print the single number — the number of the Master squares.

Sample Input :

4
5 7 8 4
9 5 3 2
1 6 6 4
9 5 7 3
Sample Output :

6
'''
n = int(input())
l = [[int(j) for j in input().split()] for i in range(n)]
x = [0 for i in range(n)]
y = [0 for j in range(n)]
c = 0
for i in range(n):
    for j in range(n):
        x[i] += l[i][j]
        y[j] += l[i][j]
for i in range(n):
    for j in range(n):
        if y[j] > x[i]:
            c += 1
print(c)

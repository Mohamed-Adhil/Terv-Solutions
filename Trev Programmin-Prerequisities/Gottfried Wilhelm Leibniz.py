'''
Gottfried Wilhelm Leibniz
Gottfried Leibniz is a founder of the binary value. Robert is a great fan of Gottfried Leibniz. He took a list of numbers and checked all the numbers in the list. If the last digit in the binary value of a number is zero he says that number is even. Else he says it as an odd number. Can you do this with a program?

Input Format : The first line contains an integer t--the number of test cases.
Then t lines consist of an integer value a.

Input Constraints : 1<=t<=10^5
1<=a<=10^7

Output Format : Print t lines of output "Yes" or "No".

Sample Input :

4
23
1412
45
2
Sample Output :

No
Yes
No
Yes
'''
for i in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print('Yes')
    else:
        print('No')

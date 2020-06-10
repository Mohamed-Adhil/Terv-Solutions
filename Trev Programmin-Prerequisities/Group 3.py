'''
Computer hardware uses binary since that is relatively simple for it. However binary is not easy for humans to read as even small numbers have a lot of binary digits.


Grouping the bits in 3 bits allows us to have shorter representations of those binary numbers since each group can be viewed easily.


Now your task is to Group the numbers as 3 from the binary number.

Input Format : The First line of input N contains a String.

Input Constraints : 1<= N <= 57, where N is the number of characters (0's and 1's) in the string.

Output Format : Single line denoting the Grouped value.

Sample Input :

10110101010010001010011
Sample Output :

26522123
'''

print(oct(int(input(), 2)).replace('0o', ''))

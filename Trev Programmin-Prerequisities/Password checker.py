'''
Password Checker
A password checker is one of the easiest projects. You just ensure some constraints and it will be ready with just 50 lines of code. One of the constraints of the password checker is to ensure a minimum of 8 letters with one uppercase letter. But none of the password checkers asks you to enter a minimum of x lowercase letters. You have made the project and now you are going to add a feature that displays the number of lowercase letters in the password.

Input Format : The only line of input contains a string.

Input Constraints : The length of the string does not exceed 10^6.

Output Format : Print a single integer.

Sample Input :

jdFEfhaAFWewu
Sample Output :

8
'''

n = input()
c = 0
for i in n:
    if i.islower():
        c += 1
print(c)

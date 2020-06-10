'''
HR Interview
In an interview, HR gave a string to a candidate and gave a task to him. He should not tell the number to anyone but have to do something to make them find the number. The candidate wrote a string in a paper and told the HR that he will give the number of occurrences of a character x in that string to every other candidate. The HR was impressed and asked him to write a program for that. Think as you were that candidate and write a program to find the count.

Input Format : The input consists of a character x and a string s of lowercase Latin letters.

Input Constraints : The length of the string does not exceed 10^6.

Output Format : Print a single integer

Sample Input :

e
terv
Sample Output :

1
'''

n = input()
s = input()
print(s.count(n))

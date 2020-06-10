'''
Essay Writing
Your essay writing homework has some constraints. It should not contain more than x number of Uppercase letters. But you are good at typing and don’t care about uppercase letters while typing. But before uploading the essay, you need to check the number of uppercase letters in the document. For that, you are going to write a program now.

Input Format: The only line of input contains a paragraph.

Input Constraints: The length of the paragraph does not exceed 10 ^ 4.

Output Format: Print a single integer

Sample Input:

A paragraph is a self-contained unit of a discourse in writing dealing with a particular point or idea.
Sample Output:

1
'''
n = input()
c = 0
for i in n:
    if i.isupper():
        c += 1
print(c)

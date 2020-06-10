'''
Love is Magic
Maths is a man(belongs to Number family) who has a daughter named Algebra. Maths always expects a logic in whatever happens. English is a man(belongs to Alphabets family) who has a son named Grammer. English always believes luck in whatever happens. Algebra fell in love with Grammar. They want to marry each other with their parents' approval. When Algebra told Maths about Grammar, Maths said “I need logic. There is no logic in combining Algebra and Grammar. And love does not have any logic”. When Grammer told English about Algebra, English said “If you are lucky Maths will accept your love”.It created a big problem between the numbers family and Alphabets family.So they called String who is common to Numbers and Alphabets to make a judgement. String wants his judgement to be accepted by people on both sides. So String said that let Algebra and Grammar tell a random number to me(x and y). I will tell you the addition (z) of the two numbers and length of the number L (L is always even). If z is a lucky number(containing 4 and 7) and if the sum of digits in the first half of z is equal to sum digits in the last half, both the family have to accept their marriage. If any one condition fails, Algebra and Grammar have to sacrifice their love. Write a program to check whether z satisfies both the condition.

Input Format : The first line contains an even integer L
The second line contains an integer z whose length is exactly equal to L

Input Constraints : 2<=L<=50
1<=z<=10^7

Output Format : Print "Yes" or "No"

Sample Input :

2
47
Sample Output :

No
'''
l = int(input())
a = input()
s1 = 0
s2 = 0
for i in range(l//2):
    s1 += int(a[i])
for j in range(l//2, l):
    s2 += int(a[j])
if s1 == s2:
    print('Yes')
else:
    print('No')

'''
Khaleesi would like to donate Clothes and Ornaments to people. She visits many villages, but she cannot donate things to everyone in the village. She have to choose certain number of people in such a way that everyone gets the same number of Clothes and Ornaments.


Help Khaleesi choose the number of people that she can donate.

Input Format : The First line of input consists of Two space separated integers N and M.
N refers to number of Clothes
M refers to number of Ornaments

Input Constraints : 1<=N<=10^7
1<=M<=10^7

Output Format : Single Integer denoting the number of people gets the same amount of Clothes and Ornaments

Sample Input :

955445098 427525248
Sample Output :

2

'''


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
print(gcd(a, b))
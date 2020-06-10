'''
Jack and Rose are going to a restaurant. Jack have lunch there every fourth day, and Rose has her lunch there every sixth day. How many days before Jack and Rose meet again for lunch at the same restaurant.

Input Format : The First line of input consists of two space separated Integers N and M.

Input Constraints : 1<=N<=10^7
1<=M<=10^7

Output Format : Single Integer denoting the number of days.

Sample Input :

608514155 771884537
Sample Output :

469702666790121235

'''


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))

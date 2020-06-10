'''
Greedy Thief
Victor is a businessman, he usually carries his money in a briefcase. This briefcase is highly secure and it is protected with a digital number lock. The briefcase is made of proto-Adamantium, an alloyed mixture of Adamantium and Vibranium. Even a blast will not be able to break it. Only Thanos has the power of breaking it.


Even though it is so secure, if anyone enters the right number combination in the number lock, it will open up. So for safety purpose, he changes the number lock everyday. Everyday, he carries a different amount in the briefcase, and he sets the lock with a minimum possible number whose sum of digits will be equal to the money present in the briefcase.


Loki, assistant of victor, wants to Steele the money and run away. He somehow came to know the money which Victor had inside the briefcase. Help Loki to identify the number lock, so he can take the money.

Input Format: One single integer N

Input Constraints: 1 <= N <= 10000000000000000000000000

Output Format: A smallest possible number whose sum of digits equals to N

Sample Input:

11
Sample Output:

29
'''
def num(x):
    su = 0
    while x != 0:
        temp = x % 10
        su += temp
        x = x//10
        return su

n = int(input())
x = n//9
a = int('9'*x)
b = n-num(a)
if b > 0:
    print(b, end='')
print(a)

'''
Chocolates for Twins
John and Dytto are close friends in college. After college, they don't get a chance to meet each other. John got married and has twin babies. Dytto wants to meet his friend. Dytto decided to buy chocolate (with n pieces) for the babies. She wants to buy one chocolate and divide it into two(a and b) so that the number of pieces in a and b are the same. The shopkeeper suggested ‘m’ number of chocolate boxes and Dytto is so confused about which box to buy. Can you help her?

Input Format : The first line contains an integer n--the number of chocolate boxes.

The second line contains n integers a1,a2,...an where ai is the number of chocolates in the i-th box.

Input Constraints : 1<=n<=10^5
0<=ai<=10^7

Output Format : Print a single integer

Sample Input :

3
1 1 2
Sample Output :

1
'''
n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
    if i % 2 == 0:
        c += 1
print(c)

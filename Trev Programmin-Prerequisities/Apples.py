'''
Every year December 23, Farmers used to celebrate Farmers Day by playing a game. Farmer Surya, places 'n' number of baskets with 'ni' apples in it. Not all the baskets are filled with same number of apples and only one basket will be removed before the game starts.


The number of apples in each basket follows a specific pattern. After removing exactly one basket, any other Farmer can approach Surya and play the game by telling the number of apples in the removed basket. If anyone tells the correct answer then that many apples will be given for free.


Arjun is now playing the game. Help Arjun find the correct number of apples in the removed basket.

Input Format : The First line consist of a single integer 'n' which corresponds to the total number of baskets after removing one basket
The Second line consists of 'n' space separated integers.

Input Constraints : 3<=n<=100
1<=a[i]<=10^4

Output Format : Single integer denoting the number of removed apples

Sample Input :

76
2595 2621 2647 2673 2699 2725 2751 2777 2803 2829 2855 2881 2907 2933 2959 2985 3011 3037 3063 3089 3115 3141 3167 3193 3219 3245 3271 3297 3323 3349 3375 3401 3427 3453 3479 3505 3531 3557 3583 3609 3635 3661 3687 3713 3739 3765 3791 3817 3843 3869 3895 3921 3947 3973 3999 4025 4077 4103 4129 4155 4181 4207 4233 4259 4285 4311 4337 4363 4389 4415 4441 4467 4493 4519 4545 4571 
Sample Output :

4051
'''

n=int(input())
l=list(map(int,input().split()))
d=l[1]-l[0]
for i in range(n-1):
    if l[i+1]-l[i]!=d:
        print(l[i]+d)

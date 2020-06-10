/*
Chocolate Truffle
Willy Wonka has N chocolate truffles with him, he wants to distribute these to N different people such that any person gets either 0, 1 or 2 truffle(s). Help Willy Wonka to evaluate the number of ways he can do this.


For example, N=2, the truffle can be distributed as {(1,1),(2,0),(0,2)}. But we will consider only the first two cases as the third case just another representation of case two.


For example, N=3, the truffle can be distributed as {(1,1,1),(2,1,0),(1,2,0),(1,0,2), (0,1,2), (2,0,1),(0,2,1)}. But we will consider only the first three cases as the other cases are just another representation of the first three cases (the order of occurance).

Input Format : Single line, containing a single integer N

Input Constraints : 1 < N < 50, where N is the number of chocolate truffles with Willy Wonka

Output Format : Single line, with single integer denoting the number of ways Willy Wonka can do this.

Sample Input :

19
Sample Output :

6765
*/

#include <stdio.h>
int main()
{
    long long int a = 0, b = 1, c, n;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    printf("%lld", c);
    return 0;
}
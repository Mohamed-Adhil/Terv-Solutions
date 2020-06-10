/*
Alwin's collection
Alwin has a Hard disk and he has n movies in that hard disk. Each movie is of different file size in GB. He wants to know the size of lowest quality movie. There is at least one lowest quality movie in the hard disk. Help him find the size of the lowest quality movie.

Input Format : The first line contains a single integer n--the number of movies in the hard disk.
The second line contains n space separated integers q1,q2,....qn where qi is the size of the i-th movie.

Input Constraints : 1<=n<=10^5
-10^7<=qi<=10^7

Output Format : Print a single integer denoting the size of the lowest quality movie.

Sample Input :

3
0 9 -1
Sample Output :

-1
*/

#include <stdio.h>
int main()
{
    long long n, min = 0, i;
    scanf("%lld", &n);
    long long a[n];
    for (i = 0; i < n; i++)
    {
        scanf("%lld", &a[i]);
    }
    min = a[0];
    for (i = 0; i < n; i++)
    {
        if (a[i] < min)
        {
            min = a[i];
        }
    }
    printf("%lld", min);
    return 0;
}
'''
Legal Marriage
In the late ’80s in Britain, the age for girls to get married was 18. In a village n unmarried females are there. Can you write a program to count the legally eligible ones to get married?

Input Format : The first line contains an integer t--the number of test case.

The first line of each test case contains an integer ni, the number of people.

The second line of each test case contains ni numbers a1,a2,....an denoting the ages.

Input Constraints : 1<=t<=10^5
1<=ni<=10^7
1<=ai<=100

Output Format : Print t lines of output, denoting the count.

Sample Input :

2
4
17 9 30 22
2
3 60
Sample Output :

2
1

'''
for i in range(int(input())):
    c=0
    n=input()
    a=list(map(int,input().split()))
    for j in a:
        if j>=18:
            c+=1
    print(c)
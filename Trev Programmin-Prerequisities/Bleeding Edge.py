'''
Bleeding Edge
Ironman and War machine a.k.a Rhodey are in a fight with enemy robots. There are n enemy robots. Ironman is wearing suit named Bleeding Edge. Bleeding Edge is widely considered to be the most powerful of them all. It is completely stored within his body. It was made on Nidavellir, Dwarven Forge World, place that created Mjolnir.


War machine is some what slower than Bleeding Edge. The fact is Bleeding Edge kills more enemies than War machine. The powers of n enemy robots are given. The fight is telecasting live on all channels. You are standing in Times Square, New york. You saw the fight. Now you are going to calculate how many enemies will be killed by Bleeding Edge. Pick Bleeding Edge some enemies such that the sum of powers of those enemies is strictly larger than the sum of powers of remaining enemies. Bleeding Edge takes the minimum number of enemies whose powers are strictly more than the sum of powers of the remaining.

Input Format : The first line contains integer n, the number of Enemies.
The second line contains a sequence of n integers a1, a2, ..., an -The powers of those enemy robots.

Input Constraints : 1<=n<=100
1<=ai<=100

Output Format : In the single line print the single number — the minimum needed number of enemies for Bleeding Edge.

Sample Input :

3
2 1 2
Sample Output :

2
'''
n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
m = sum(l)//2
s = 0
i = 0
while s <= m:
 s += l[i]
 i += 1
print(i)

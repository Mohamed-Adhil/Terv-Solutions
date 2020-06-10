'''
Noodle King
Food festival is when we get to taste multiple cuisines at one place. There is a chef called Victor, from Eastern Europe. He is specialized in making noodles.


Noodle is tastier with how long it is.  This noodle is a special type of noodle, each meter of noodle weighs 100 grams. Victor conducts small games, and the game will be conducted in multiple levels, and each level of game, the person will be awarded one meter of this special noodle. If a person looses at a particular level, then he will be giving the noodle which he won, and paying an amount to him for cooking that quantity of noodle which he won during the contest. At the end of each level the person must be given the particular amount of noodle as the reward. As you know, noodle is longer the better. So, brake the noodles for minimum number of times so that it will be tastier while cooking it but at the same time at the end of each level the particular reward must be given to the participant.


N meters of noodle is available with the chef, so he can conduct a game which has N levels, so that he can give a meter of noodle as a gift for successfully completing each level. Help Victor with the minimum number of times he must brake the noodles.

Input Format : One single integer input N, where N corresponds to the number of levels in the competition conducted by the chef

Input Constraints : 1<=N<=10^18
where N is the number of levels in the competition

Output Format : One single integer output corresponding to the number of times the chef has to brake the noodle

Sample Input :

28374682737832
Sample Output :

44
'''

n = int(input())
c = 0
while n > 0:
    n = n//2
    c += 1
print(c-1)

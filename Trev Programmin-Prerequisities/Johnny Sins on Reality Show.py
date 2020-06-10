'''
Johnny Sins on Reality Kings
Johnny Sins is going to participate in a game TV show called Reality Kings. The game is popularly known as  Me vs N.


The game goes in rounds, where in each round the host asks Johnny and his opponents a common question. All participants failing to answer are eliminated. The show ends when only Johnny remains (we assume that Johnny never answers a question wrong!).


For each question Johnny answers, if there are R (R>0) opponents remaining and T (0≤T≤R) of them make a mistake on it, Johnny receives t/R dollars, and consequently there will be R−T opponents left for the next question.


Johnny wonders what is the maximum possible reward he can receive in the best possible scenario. Yet he has little time before show starts, so can you help him answering it instead?

Input Format : The first line contains an integer N, the number of Johnny's opponents in the show.

Input Constraints : 1<=N<=10^5

Output Format : Print a number denoting the maximum prize (in dollars) Johnny could have.

Your answer will be considered correct if it's absolute or relative error won't exceed 10^4.

Sample Input :

2
Sample Output :

1.5
'''
r = int(input())
t = 1
d = 0
while r > 0:
    d += (t/r)
    r = r-t
print("%0.1f" % d)

'''
Dictionary
We all know some of the greatest dictionaries in the world like the Oxford English Dictionary or the Cambridge English Dictionary so on and so forth. Ram, an English enthusiast who also happens to be a very good programmer is very interested in building a digital dictionary. He would like to add a feature to the digital dictionary that he believes is "cool". Here is an excerpt that describes this feature.


Given any sequence of characters between 'a' and 'z' (both inclusive), the tool needs to return the row in which the word will possibly occur if all the possible arrangements of the given sequence is taken and arranged lexicographically.

Since Ram is busy building the other features of the digital dictionary, you have been given the job of building this "cool" feature.

Input Format : The only line of input contains the string S.

Input Constraints : 1 ≤ |S| ≤ 20
'a' ≤ S[i] ≤ 'z'

Output Format : Print a single integer denoting the Rank of the Word.

Sample Input :

word
Sample Output :

22
'''

fact = [1]
for i in range(1, 21):
    fact.append(i * fact[i-1])

s = input()
n = len(s)
a = [0 for i in range(26)]
for x in s:
    a[ord(x) - ord('a')] += 1
res = 0
for i in range(n):
    for j in range(ord(s[i])-ord('a')):
        if(a[j]==0): continue
        r = 1
        a[j] -= 1
        for k in range(26):
            if(a[k]>0):
                r *= a[k]
        res += (fact[n - (i+1)] // r)
        a[j] += 1
    a[ord(s[i]) - ord('a')] -= 1
print(res + 1)

'''
Mars Astronauts 2
By definition, a sidereal day on Mars is the length of time that it takes the planet to rotate once on its axis so that stars appear in the same place in the night sky. On Earth, this takes exactly 23 hours, 56 minutes and 4.1 seconds. In comparison, on Mars, a sidereal day lasts 24 hours, 37 minutes, and 22 seconds.You are part of the Mars astronauts team and you could be able to convert any earth time into Mars time in mind. Before that, you have to verify the Earth time. Write a program for that. If verification is true then you can convert it to Mars time in mind.


Input Format : The input contains a time in HH:MM:SS format.

Input Constraints : A time.

Output Format : Print "Valid" or "Invalid"

Sample Input :

12:62:00
Sample Output :

Invalid
'''

h, m, s = map(int, input().split(':'))
if h >= 0 and h < 24 and m >= 0 and m < 60 and s >= 0 and s < 60:
    print('Valid')
else:
    print('Invalid')

'''
Mars Astronauts 1
By definition, a sidereal day on Mars is the length of time that it takes the planet to rotate once on its axis so that stars appear in the same place in the night sky. On Earth, this takes exactly 23 hours, 56 minutes and 4.1 seconds. In comparison, on Mars, a sidereal day lasts 24 hours, 37 minutes, and 22 seconds. You are part of the Mars astronauts team and you could be able to convert any earth date into Mars date in mind. Before that, you have to verify the Earth date. Write a program for that. If verification is true then you can convert it to Mars date in mind.


Input Format : The input consists of a date in dd/mm/year format.

Input Constraints : A date.

Output Format : Print "Valid" or "Invalid"

Sample Input :

12/04/2020
Sample Output :

Valid
'''
d, m, y = map(int, input().split('/'))
a = 0
if d <= 31 and d > 0 and m <= 12 and m > 0 and y > 0:
 if m == 1 and d <= 31:
  a = 1
 if m == 2 and d <= 29:
  if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
   a = 1
  elif d <= 28:
   a = 1
 if m == 3 and d <= 31:
  a = 1
 if m == 4 and d <= 30:
  a = 1
 if m == 5 and d <= 31:
  a = 1
 if m == 6 and d <= 30:
  a = 1
 if m == 7 and d <= 31:
  a = 1
 if m == 8 and d <= 31:
  a = 1
 if m == 9 and d <= 30:
  a = 1
 if m == 10 and d <= 31:
  a = 1
 if m == 11 and d <= 30:
  a = 1
 if m == 12 and d <= 31:
  a = 1
if a == 1:
 print('Valid')
else:
 print('Invalid')

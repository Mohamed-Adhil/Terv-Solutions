'''
A transponder (short for transmitter-responder and sometimes abbreviated to XPDR,XPNDR,TPDR or TP) is an electronic device that produces a response when it receives a radio-frequency interrogation. Aircraft have transponders to assist in identifying them on air traffic control radar. Collision avoidance systems have been developed to use transponder transmissions as a means of detecting aircraft at risk of colliding with each other. Air traffic control units use the term "squawk" when they are assigning an aircraft a transponder code, e.g., "Squawk 7421". Squawk thus can be said to mean "select transponder code" or "squawking xxxx" to mean "I have selected transponder code xxxx”. The transponder receives interrogation from the Secondary Surveillance Radar on 1030 MHz and replies on 1090 MHz. [wiki]


The 4 digit transponder code can be used to uniquely identify upto 4096 aircrafts. The digital systems in the ATC (Air Traffic Controller) however, cannot understand the radix used by the transponders in aircrafts. Your job is to take the transponder code and convert it into a radix that can be understood by the digital systems in ATC.

Input Format : Single line containing several aircraft codes concatenated together.

Input Constraints : 1<= N <= 19, where N is the number digits in the concatenated aircraft code.

Output Format : Single line containing the transponder codes in a radix that can be understood by the digital systems in ATC.

Sample Input :
2
Sample Output :
10
'''

print(bin(int(input(), 8)).replace('0b', ''))

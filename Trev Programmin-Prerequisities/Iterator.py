'''
Iterator
Given a number N followed by N integers, it will comprise of certain positive numbers, then a zero then follows negative numbers. Find the minimum number of iterations to convert a Positive-Zero-Negative array into a Negative-Zero-Positive array, by abiding by the given constraints.



Constraints for Swapping:

1. Swapping is possible only with a Zero

2. A positive number should be swapped only to the right hand side

3. A negative number should be swapped only to the left hand side

4. Swapping can be done to a maximum of two steps at a time.



Find the minimum number of iterations.

Input Format : The first line of input has a single integer value N followed by N integer values.

Input Constraints : 3<=N<=2500 -1000<=a[i]<=1000 Where N is the number of elements of the array and a[i] is each element of the array.

Output Format : One single integer denoting the number of iterations required.

Sample Input :

348
236 167 776 769 752 381 648 23 968 687 837 733 656 481 659 608 913 25 750 474 876 574 410 942 390 230 869 332 523 658 536 243 189 412 984 318 986 532 321 588 376 883 788 258 434 896 838 201 129 363 626 628 793 94 768 710 53 169 106 679 470 356 537 72 978 647 182 185 158 830 121 946 785 87 979 657 953 358 478 588 280 300 895 596 3 952 184 325 712 711 237 474 815 541 714 166 50 730 569 309 418 857 624 680 480 838 443 153 900 702 492 629 520 196 871 170 224 436 430 267 345 433 850 394 132 4 60 192 262 547 805 104 296 4 589 557 340 653 316 682 973 186 855 980 659 422 647 284 265 781 296 410 539 318 921 857 138 531 75 14 140 443 875 73 786 686 0 -2 -452 -224 -857 -700 -854 -536 -710 -541 -873 -962 -365 -385 -175 -937 -845 -722 -108 -893 -782 -462 -346 -140 -728 -971 -308 -400 -421 -626 -434 -775 -161 -501 -974 -605 -893 -171 -848 -767 -146 -788 -523 -788 -392 -962 -290 -828 -314 -701 -45 -317 -323 -956 -805 -14 -416 -326 -982 -99 -168 -959 -450 -862 -544 -274 -401 -412 -380 -917 -991 -533 -759 -967 -1000 -859 -675 -130 -663 -251 -759 -73 -632 -405 -776 -193 -980 -690 -433 -369 -518 -666 -758 -884 -127 -9 -355 -507 -853 -840 -304 -208 -584 -562 -527 -175 -566 -379 -503 -749 -524 -596 -761 -860 -111 -950 -834 -16 -407 -79 -420 -586 -830 -58 -523 -979 -646 -364 -496 -700 -283 -543 -241 -219 -327 -169 -262 -252 -231 -330 -314 -650 -331 -731 -523 -502 -185 -395 -458 -181 -222 -708 -47 -999 -941 -507 -896 -773 -952 -516 -240 -53 -783 -696 -326 -541 -170 -280 -556 -889 -155 -510 -145 -233 -291 -663 -532 -31 -270 -521 -672 -863
Sample Output :

30393
'''
n = int(input())
l = list(map(int, input().split()))
po = 0
ne = 0
for i in l:
    if i > 0:
        po += 1
    elif i < 0:
        ne += 1
print(po*ne+n-1)

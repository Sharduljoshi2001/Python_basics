"""
Name – AYTIJHA CHAKRABORTY
Student ID – 19011511
University Roll Number – 1914009
BTech (2nd Year) – Section K

Question: To print the nth Even and Odd numbers.
"""

n = int(input("Enter n: "))
ev = 2*n
od = (2*n)-1
if (n % 10 == 1):
    print("{}st Even Number = {}\n{}st Odd Number = {}".format(n, ev, n, od))
elif (n % 10 == 2):
    print("{}nd Even Number = {}\n{}nd Odd Number = {}".format(n, ev, n, od))
elif (n % 10 == 3):
    print("{}rd Even Number = {}\n{}rd Odd Number = {}".format(n, ev, n, od))
else:
    print("{}th Even Number = {}\n{}th Odd Number = {}".format(n, ev, n, od))
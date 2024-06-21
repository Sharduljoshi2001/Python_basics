"""
Name – SHARDUL JOSHI
University Roll Number – 1102869
MCA (1st year) – Section A

Question: Take the age of the user as Input. If the user is eligible for vote then take some Voter ID as an input.
If the ID is at least 6 digits long, then print "Vote Done", Otherwise print an appropriate error message.
"""

import math
age = int(input("Enter your age: "))
if (age>=18):
    print("You are eligible to vote")
    id = int(input("Enter your Voter ID: "))
    if (math.log10(id) >= 5):
        print("Vote Done")
    else:
        print("Invalid Voter ID")
else:
    print("You are not eligile to vote")

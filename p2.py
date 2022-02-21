"""
Name – AYTIJHA CHAKRABORTY
Student ID – 19011511
University Roll Number – 1914009
BTech (2nd Year) – Section K

Question: To print the Reverse of a number.
"""

n = int(input('Enter a number: '))  
rev = 0  
while (n>0):  
    # Logic  
    rem = n % 10  
    rev = (rev * 10) + rem  
    n //= 10  
print('Reversed number is: ', rev)
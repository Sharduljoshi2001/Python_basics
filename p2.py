"""
Name – SHARDUL JOSHI
University Roll Number – 1102869
MCA (1st year) – Section A

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

"""
Name – AYTIJHA CHAKRABORTY
Student ID – 19011511
University Roll Number – 1914009
BTech (2nd Year) – Section K

Question: To print all Armstrong numbers between 2 numbers.
"""

low = int(input('Enter the lower limit: '))
high = int(input('Enter the higher limit: '))
print('All Armstrong numbers between {} and{} are:'.format(low, high))
while (low < high):
    power = len(str(low))
    sum = 0
    num = low
    while num > 0:
        temp=num%10
        sum+=temp**power
        num//=10
    if low == sum:
        print(low)
    low += 1
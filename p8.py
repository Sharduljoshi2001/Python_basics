"""
Name – SHARDUL JOSHI
University Roll Number – 1102869
MCA (1st year) – Section A

Question: To print the longest palindrome in a given string.
"""

str=[] # list containing all strings
l=[] # list containing length of palindrome strings
c=[] # list containing the palindrome strings
n=int(input('Enter the number of strings present in the list: '))
for i in range(n):
  s=input('Enter any string: ')
  str.append(s)  
for strin in str:
  if strin==strin[::-1]:
    l.append(len(strin))
    c.append(strin)
l.sort(reverse=True)
d=l[0]
for i in c:
  if d==len(i):
    print(i, 'is the longest pallendrome in the string')
    break

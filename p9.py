"""
Name – AYTIJHA CHAKRABORTY
Student ID – 19011511
University Roll Number – 1914009
BTech (2nd Year) – Section K

Question: To find the product of all tuples inside a tuple, and find the max and min product.
"""

tup = ((8,4),(6,5),(7,8),(9,3))
res = []
count=0
for i in tup:
  mul=1
  val = tup[count]
  for j in i:
    mul *= j
  res.append(mul)
  count += 1
print (max(res))
print (min(res))
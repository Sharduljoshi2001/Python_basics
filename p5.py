"""
Name – AYTIJHA CHAKRABORTY
Student ID – 19011511
University Roll Number – 1914009
BTech (2nd Year) – Section K

Question: To demonstarte String handling.
"""

str = "Naruto Shippuden is the best Anime"
print (str)
print (len(str))
print (str[3:21:2])
if "Anime" in str:
    print ("The Sage of Six Paths")
print (str.upper())
print (str.lower())
print (str.split(" "))
for i in "Naruto":
    print (i)
str1 = "*****Demon *** Slayer*****"
print (str1.strip("*"))
print (str1.lstrip("*"))
print (str1.rstrip("*"))
print (str + " " + str1)
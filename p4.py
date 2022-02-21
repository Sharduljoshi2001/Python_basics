"""
Name – AYTIJHA CHAKRABORTY
Student ID – 19011511
University Roll Number – 1914009
BTech (2nd Year) – Section K

Question: To show the functioning and operations related to Dictionaries.
"""

d_anime = {
  "Naruto": "Sasuke",
  "Bakugo": "Midoriya",
  "Asta": "Yuno"
}
print (d_anime)
print (d_anime.keys())
print (d_anime.values())
print (d_anime.items())
d_anime.update({"Bakugo": "Deku"})
print (d_anime)
print (d_anime["Naruto"])
d_anime["Goku"] = "Vegeta"
print (d_anime)
d_anime.pop("Goku")
print (d_anime)
d_anime.clear()
print (d_anime)
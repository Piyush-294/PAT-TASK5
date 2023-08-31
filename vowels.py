x = "guvi geeks network private limited"
vowel_count = 0
i = ["a", "e", "i", "o", "u"]
for char in x:
    if char in i:
        vowel_count += 1
print("number of vowels are:",vowel_count)
a = x.count("a")
print("a =", a)
e = x.count("e")
print("e =", e)
i = x.count("i")
print("i =", i)
o = x.count("o")
print("o =", o)
u = x.count("u")
print("u =", u)



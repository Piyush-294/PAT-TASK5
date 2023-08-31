"""alternate method without using function
this is a multi line comment"""


# x = input("enter str1:")
# m = list(x)
# m.sort()
# y = input("enter str2:")
# n = list(y)
# n.sort()
# if m==n:
#     print("it is anagram")
# else:
#     print("it is not an anagram")

def anagram(x, y):
    m = list(x)
    m.sort()
    n = list(y)
    n.sort()
    if m == n:
        print(m == n, ", it is anagram")
    else:
        print(m == n, ", it is not an anagram")


x = input("enter str1:")
y = input("enter str2:")
anagram(x, y)

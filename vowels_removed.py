# logic without using function
# a = input("enter any string:")
# b = ""
# i = ["a", "e", "i", "o", "u"]
# for char in a:
#     if char not in i:
#       b = b + char
# print(b)
def vowels_removed(string):
    i = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in i:
           string = string.replace(char, '')
    print(string)
string = input("enter any string:")
vowels_removed(string)
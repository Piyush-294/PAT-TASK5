# logic without function
# a = input("enter any string:")
# b = a[-1::-1]
# if b == a:
#     print("true", "it is a palindrome")
# else:
#     print("false", "it is not a palindrome")

def palindrome(string):
    b = string[::-1]
    if b == string:
        print(b==string,"it is a palindrome")
    else:
        print( b==string, "it is not a palindrome")
        # return b
string= input("enter any string:")
print(string)
palindrome(string)
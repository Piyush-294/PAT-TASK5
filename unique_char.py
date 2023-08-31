def unique_char(string):
    unique_string = []
    for char in string:
        if char not in unique_string:
            unique_string.append(char)
        print("the output is:",unique_string)

string = input("enter any string:")
unique_char(string)
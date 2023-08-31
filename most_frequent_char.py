from collections import Counter
def freq_char(string):
    result = Counter(string)
    result = max(result, key=result.get)
    print(result)
string = input("enter any string:")
freq_char(string)
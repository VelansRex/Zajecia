# 1. Write a Python program to calculate the length of a string.

def string_length(str1):
    count = 0
    for i in str1:
        count = count + 1

    return count

print(string_length("Paweł"))
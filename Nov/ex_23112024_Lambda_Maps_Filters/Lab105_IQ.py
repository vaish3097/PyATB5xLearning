#print non repeating char in a string using set

def first_non_repeating(string):
    for char in string:
        if string.count(char)==1:
            return char
    return None
print(first_non_repeating('swiss'))

str="vaishnavi"

set1=set(str)


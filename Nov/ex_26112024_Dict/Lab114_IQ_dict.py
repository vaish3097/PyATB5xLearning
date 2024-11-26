#Remove duplicate values from dict

my_dict={"a":1,"b":2,"c":3,"a":1}
set1=set()
set2=set()
result={}
for key, value in my_dict.items():
    set1.add(key)
    set2.add(value)
list1= list(set1)
list2= list(set2)

output= dict(zip(list1, list2))
print(output)

#  Remove duplicate values from a dictionary.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
# Output: {'a': 1, 'b': 2, 'd': 3}

unique_value = set()

result = {}
for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

print(result)



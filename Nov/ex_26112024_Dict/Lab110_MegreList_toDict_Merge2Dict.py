
# merge 2 list with zip
keys=["name","age","ROLE"]
values=["Vaish", 27, "MT"]

dict1= dict(zip(keys, values))
print(dict1)
'''
#Merge 2 dictionaries
stu_info1 = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "experience": 3
}


stu_info2 = {
    "name": "Vaish",
    "age": 27,
    "role": "Manual tester",
    "experience": 3
}

res= stu_info1 | stu_info2
print(res)

# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)
'''

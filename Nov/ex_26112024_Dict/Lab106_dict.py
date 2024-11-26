my_dict= {"name":"Vaish", "age":27, "home":"Lucknow"}
print(my_dict)

for key,value in my_dict.items():
    print(key, "->", value)

my_dict["role"]="Manual tester"
print(my_dict)

my_dict["address"]={"home":"ND", "Office":"KA"}
print(my_dict)

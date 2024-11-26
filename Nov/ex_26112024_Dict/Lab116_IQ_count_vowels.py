str="hello world! Good Morning"

count=0
vowels='aeiou'

for char in str:
    if char in vowels:
        count=count+1
print(count)

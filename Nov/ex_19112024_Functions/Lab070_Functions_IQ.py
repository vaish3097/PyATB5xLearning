#Create a program to sum of 3 numbers


def sum_of_three_numbers(a=100,b=200,c=300):
    return(a+b+c)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
res=sum_of_three_numbers(a,b,c)
res1=sum_of_three_numbers()
print(f"Sum of 3 numbers with user input {res}")
print(f"Sum of 3 numbers with default agrument {res1}")
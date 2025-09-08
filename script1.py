n= int(input("enter a number here:"))
def factorial(n):
    if n<2 and n>=0:
        return 1
    else:
        return n*(factorial(n-1))
r=factorial(n)
print(r)
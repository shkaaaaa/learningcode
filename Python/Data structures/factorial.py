# i=int(input("Enter a number: "))
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print(f"Facotiral of given number is {fac}")

def factorial(a):
    fac=1
    for i in range(a,0,-1):
        fac=fac*i
    return fac
n=int(input("Enter a number: "))
res=factorial(n)
print("Factorial of",n,"is",res)
    
def square(a):
    return a**2
def squareroot(b):
    return b**(1/2)
def pythagoras(a,b):
    c = ((square(a))+(square(b) ))**(1/2)
    return c
result = pythagoras(6,6)
print(result)


# n = int(input("Enter a number:"))
# print(f"Square is {square(n)} and Squareroot is {squareroot(n)}")
# square_value=square(n)
# sqroot=squareroot(n)
# print(f"Square is {square_value} and Squareroot is {sqroot}")   

def square(a):
    print(a*a)
def squareroot(b):
    print(b**(1/2))
n = int(input("Enter a number:"))
square(n)
squareroot(n)  
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b:
    if a>c:
        print(f"Greater number is: {a}")
    else:
        print(f"Greater number is: {c}")
else:
    if b>c:
        print(f"Greater number is: {b}")
    else:
        print(f"Greater number is: {c}")
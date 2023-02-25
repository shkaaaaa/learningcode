while True:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print(''' WELCOME TO CALCULATOR 
    1. Addition
    2. Substraction
    3. Division
    4. Multiplication
    5. Modulus
    6. Quotient
    7. Close\n''')
    choice = int(input("Enter your choice: "))

    if choice==1:   
        print(first+second)
    elif choice==2: 
        print(first-second)
    elif choice==3:
        print(first/second)
    elif choice==4:
        print(first*second)
    elif choice==5:
        print(first%second)
    elif choice==6:
        print(first//second)
    elif choice==7:
        break
    else:
        print("Wrong choice")
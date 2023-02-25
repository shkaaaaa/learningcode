try:
    a=1/0
    print(a)
except ValueError:
    print("Invalid operation")
   
finally:
    print("finally this")
    
def sum():
    sum=0
    while sum<100:
        try:
            user=int(input("Enter a number"))

            sum+=user
            print(sum)
        except ValueError:
            print("Invalid input")
        except ZeroDivisionError:
            print("Divided by 0")
        finally:
            print("U are ready to add new no.")
sum()
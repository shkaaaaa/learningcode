def linearSearch(numbers,user):
    flag=0
    for i in numbers:
        if user==i:
            flag=1
    if flag:
        print("yes")
    else:
        print("no")

def largestNumber(numbers):
    biggest=numbers[0]
    for i in numbers:
        if biggest<i:
            biggest=i
    print(biggest)
    
    
def smallestNumber(numbers):
    smallest=numbers[0]
    for i in numbers:
        if smallest>i:
            smallest=i
    print(smallest)


numbers=[22,33,44,-23,55,66,77,88]
smallestNumber(numbers)

# user=int(input("Enter a number :"))
# linearSearch(numbers,user)
# largestNumber(numbers)

# largest=largestNumber(numbers)
# print(largest)
    
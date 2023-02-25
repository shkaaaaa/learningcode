# start = 100
# end = 500
# print("Prime numbers between",start, "and",end,"are: ")
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#            if (num%i)==0:
#             break
#         else:
#             print(num)

# def greet(name):
#     print("Hello")
#     return
#     print("How uh doing?",name)
# greet("Anushka")

# def add_numbers(x,y):
#     result = x+y
#     return result
# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# result=add_numbers(n1,n2)
# print("The sum is:",result)

# marks=[45,60,35,72,80,55]
# length=len(marks)
# print("The length is:",length)
# marks_sum = sum(marks)
# print("The sum of marks is:",marks)

#find the average marks
# def average_marks(marks):
#     sum_marks=sum(marks)
#     total_subjects=len(marks)
#     average=sum_marks/total_subjects
#     return average
# def compute_grade(average):
#     if average>=80:
#         grade="A"
#     elif average>=60:
#         grade="B"
#     elif average>=50:
#         grade="C"
#     else:
#         grade="D"
#     return grade

# marks=[55,64,75,80,65]
# average=average_marks(marks)
# print("The average marks are:",average)
# grade=compute_grade(average)
# print("The grade is:",grade)

#task
def add_numbers(n,m):
    result=n+m
    return result
def mul_numbers(n,m):
    result=n*m
    return result
n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
result=add_numbers(n,m)
result=mul_numbers(n,m)
print("Addition is: ",result)
print("Multiplication is:",result)
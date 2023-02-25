#1.water consumption problem
# n = int(input("Enter water drank by chef"))
# if n >= 2000:
#     print("Advice followed")
# else:
#     print("Advice not followed")

# 2.add two integers number
# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# c = a+b
# print(c)

# 3.LUDO problem
# n = int(input("Enter a number chef rolled"))
# if n == 6:
#     print("Chef can enter new token into play")
# else:
#     print("Chef cannot enter new token into play")

# 4.Squats problem
# n = int(input("Enter number of sets"))
# print(15 * n)

#5.Fitness problem
# n = int(input("Enter distance from office to home"))
# m = 2 * n
# print(5 * m)

# 6.Biryani problem
# n = int(input("Enter number classes chef attended")) 
# m = 10 #cost of classes per week
# print(n * m)

# 7.praclist 
# n = int(input("Enter the count of all problems"))
# m = int(input("Enter already attempted problems"))
# print(n - m)

# 8.Tax in chefland
# n = int(input("Enter total income in rupees"))
# if n >100:
#     print(n - 10)

# 9.audible problem
# n = int(input("Enter frequency in hertz"))
# if n >=65 and n <=45000:
#     print("Can hear")
# else:
#     print("Cannot hear")

# n = int(input("Enter number of hours"))
# m = n * 60
# print(m // 20)
 
# x = int(input("Enter number of courses :"))
# y = int(input("Enter number of units in each course :"))
# z = int(input("Enter number of chapters in each unit: "))
# print(f"Total number of chapters are {x*y*z}")

# x = int(input("Enter current difficulty level: "))
# y = int(input("Enter question difficulty: "))
# if y >=x and y <=(x+200):
#     print("yes")
# else:
#     print("No")

# n = int(input("Enter discount in percent: "))
# m = 100 * (n/100)
# print(100 - m)

# a = int(input("Enter value of Nr: "))
# b = int(input("Enter value of Dr: "))
# if a >= b:
#     print(a)
# else:
#     print(b)

# a = int(input("Enter marks of section A: "))
# b = int(input("Enter marks of section B: "))
# c = int(input("Enter marks of section C: "))
# if (a+b+c)>=100 and a>=10 and b>=10 and c>=10:
#     print("Pass")
# else:
#     print("Fail")

# a = int(input("Enter cost of first TV"))
# b = int(input("Enter cost of second TV"))
# c = int(input("Enter discount on first TV"))
# d = int(input("Enter discount on second Tv"))
# first_tv = a - c
# second_tv = b - d 
# if first_tv < second_tv:
#     print("First TV is cheaper")
# elif first_tv == second_tv:
#     print("Either")
# else:
#     print("Second TV is cheaper")

# R1 = int(input("Enter decision of first referee"))
# R2 = int(input("Enter decision of second referee"))
# R3 = int(input("Enter decision of third referee"))
# R4 = int(input("Enter decision of forth referee"))
# if R1 == 1 and R2 == 1 and R3 == 1 and R4 == 1:
#     print("IN")
# else:
#     print("OUT")

# x = int(input("Enter daily intake of tea"))
# y = int(input("Capacity of jar in ltr"))
# z = int(input("Enter amount for each refill"))
# refill = (x//y)+1
# # capacity = y
# # if x <= y:
# #     pass
# # elif x > y:
# #     while (y < x):
# #         y = y + capacity
# #         refill = refill+1
# print(refill * z)

# HOMEWORK.3
# a = int(input("Enter marks of first subject"))
# b = int(input("Enter marks of second subject"))
# c = int(input("Enter marks of third subject"))
# avg_score1 = a+b/2
# avg_score2 = b+c/2
# avg_score3 = a+c/2
# if avg_score1<35 or avg_score2<35 or avg_score3<35:
#     print("Fail")
# else:
#     print("Pass")

n = int(input("Enter the number of friends"))
x = int(input("Enter the number of slices needed"))
total_slice=n * x
if total_slice%4==0:
    print(total_slice/4)
else:
    print((total_slice//4)+1)

# n = int(input("Enter problems submitted by munchy"))
# m = int(input("Enter problems approved by chef"))
# if (n/2)<m:
#     print("expert")
# else:
#     print("not expert")


# n = int(input("Enter a number"))
# # for i in range(1,n+1):
# #     if (i*2)>=n:
# #         break
# #     print(i*2)
# # print("completed")

# def even(n):
#     for i in range(1,n+1):
#         if(i*2)>=n:
#             break
#         print(i*2)
#     return 1

# even(n)
# value=even(n)
# print(value)




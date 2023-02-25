# check if provided value is greater than 10 or greater tgan 20
n = int(input("Enter a car speed"))

# if n < 10:
#     print("none")
# elif n >10 and n<20:
#     print("10 rupees")
# elif n> 20 and n<30:
#     print("20 rupees")
# else:
#     print("30 rupees")

# two_remainder=n%2
# three_remainder=n%3
# if two_remainder==0 or three_remainder==0:
#     print("divisible")
# else:
#     print("not divisible")

#if car speed is less than 30 print slow,if its greater than 30 and less than 60 print medium,if its greater than 60 print fast

if n < 30:
    print("slow")
elif n >30 and n <60:
    print("medium")
else:
    print("fast")

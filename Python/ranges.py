def ranges(a,b):
    arr=[]
    while a!=b:
        arr.append(a)
        a+=1
    return arr

for i in ranges(2,8):
    print(i)
    
for i in [2,3,4,5,6,7]:
    print(i)
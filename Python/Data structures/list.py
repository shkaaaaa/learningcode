names=["Anushka","Sandip","Kittu","Mom","Dad"]
names.insert(1,"food")
flag=0
for i in names:
    if i=="Kittu":
        flag=1
if flag:
    print("true")
else:
    print("false")
    

if "Kittu" in names:
    print("true")
    
for i in range(0,len(names)):
    if names[i]=="Kittu":
        print("true")
    
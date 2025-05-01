a=[1,2,3,4,5,6,7]
find=int(input("Enter Element:"))
ind=0
for i in a:
    if find is i:
        print(ind," is the index")
    ind+=1

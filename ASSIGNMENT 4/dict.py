n=int(input("Enter no. of key value pair: "))
d={}
for i in range(n):
    k=input("Key: ")
    v=input("Value: ")
    d[k]=v
t=list(d.items())
print("List of tuples: ", t)

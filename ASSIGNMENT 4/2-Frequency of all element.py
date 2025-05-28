'''n=int(input("Enter no. of key value pair: "))
d={}
f={}
for i n range(n):
    k=input("Keys: ")
    v=input("Values: ")
    d[k]=v
for i in d.values():
    if i in f:
        f[v]+=1
    else:
        f[v]=1
print("Frequency of values: ")
for j in f:
    print(j, ":", f[j])
'''

t = "Delulu person\n dont worry\nhello world"
print(t)
n = t.split('.')
n += t.split('!')
n += t.split('?')
n = [s.strip() for s in n]

count = 0
for i in n:
    if i.lower().startswith('d'):
        count += 1

print("Number of sentences starting with 'd':", count)


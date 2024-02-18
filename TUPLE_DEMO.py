t=(10,20,1,1,1.1,[100,200,300],2.2,"tops",True)

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)
print(t[5])
t[5].append(400)
print(t)

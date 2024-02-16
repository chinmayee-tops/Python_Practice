d={101:"Banana",908:"Apple",675:"Grapes"}

print(d[908])
print(d.get(675))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(101))
print(d)
d.popitem()
print(d)
d1={1:"apple",2:"cherry",3:"orange"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])

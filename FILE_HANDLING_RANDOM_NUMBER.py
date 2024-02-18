

import random

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+" , ")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

l=data.read().split(",")[:-1]

#print(l)

for i in l:
    if int(i)%2==0:
        even.write(i+" , ")
    else:
        odd.write(i+" , ")

data.close()
even.close()
odd.close()

print("Contents from Data File")
data=open("data.txt","r")
print(data.read())
data.close()

print("Contents from Even File")
data=open("even.txt","r")
print(data.read())
data.close()

print("Contents from Odd File")
data=open("odd.txt","r")
print(data.read())
data.close()



import random

#print(random.randint(1,100))
#print(random.choice([1,2,3,4,"tops",True,10,20]))

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")


data.close()
even.close()
odd.close()


print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even File Content")
data=open("even.txt","r")
print(data.read())
data.close()

print("Odd File Content")
data=open("Odd.txt","r")
print(data.read())
data.close()

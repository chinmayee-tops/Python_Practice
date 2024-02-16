a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print(a," Is Max")
    else:
        print(c," Is Max")
elif b>c:
    print(b," Is Max")
else:
    print(c," Is Max")

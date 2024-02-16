class Add:
    def getdata(self, a, b):
        self.a=a;
        self.b=b;

    def putdata(self):
        print(" a: ",self.a)
        print(" b: ",self.b)

    def sum(self):
        self.sum=self.a+self.b;
        print("Sum : ",self.sum)

    def sub(self):
        self.sub=self.a-self.b;
        print("Sub : ",self.sub)


A1=Add()
A1.getdata(10, 40)
A1.putdata()
A1.sum()
A1.sub()

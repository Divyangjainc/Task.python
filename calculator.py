class airtel:
    # class variable
    a = 12
    b = 90

    # class methods
    def add(self) :
        return self.a+self.b;
    def mul(self) :
        return self.a*self.b;
    def div(self) :
        return self.a/self.b;
    def sub(self) :
        return self.a-self.b;


obj = airtel()
print(obj.a)
print(obj.b)
print("addition", obj.add())

obj = airtel()
print(obj.a)
print(obj.b)
print("multiplication" ,obj.mul())

obj = airtel()
print(obj.a)
print(obj.b)
print("division" ,obj.div())

obj = airtel()
print(obj.a)
print(obj.b)
print("subtraction" ,obj.sub())


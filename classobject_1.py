class Sample:
    # class variable
    a = 12
    b = 90


    # class methods
    def add(self):
        return self.a+self.b;

obj = Sample()
print(obj.a)
print(obj.b)
print("addition" ,obj.add())    


    

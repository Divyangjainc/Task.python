class Sucess:
    #class variable
    a = 5
    b = 7


    # class methods
    def mul(self) :
        return self.a*self.b;

obj = Sucess()
print(obj.a)
print(obj.b)
print("multiplication" , obj.mul())

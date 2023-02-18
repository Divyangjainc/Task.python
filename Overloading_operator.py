class A:

    def __init__(self,a):
        self.num=a

    def __add__(self,b):
        return self.num+b.num

obj1 = A(89)
obj2 = A(4)

print("Addition : ",obj1+obj2)

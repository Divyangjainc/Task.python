class Airtel:

    def __init__(self,a):
        self.value = a


    def display(self):
         print("Name = ",self.value)

name = input()
age = Airtel(name)
age.display()

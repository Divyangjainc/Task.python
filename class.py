class my_class:

    def display(self):
        print("Display Class")


class my_friend:

    def display(self):
        print("Friend Class")

print("----------MyClass Class----------")
abc = my_class()
print("Using Abc Object : ")
abc.display()

Sucess = my_class()
print("Using Sucess Object : ")
Sucess.display()

print("----------MyFriend Class----------")
airtel = my_friend()
print("Using Airtel Object : ")
airtel.display()

Switch = my_friend()
print("Using Switch Object : ")
Switch.display()

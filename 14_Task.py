class Airtel:
        def __init__(self, name, age, gender, email, contact, address):
            self.name = name
            self.age = age
            self.gender = gender
            self.email = email
            self.contact = contact
            self.address = address


        def display(self):
            print("Name: ", self.name)
            print("Age: ", self.age)
            print("gender: ", self.gender)
            print("email: ", self.email)
            print("contact: ", self.contact)
            print("address: ", self.address)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
email = input("Enter your email: ")
contact = int(input("Enter your contact number: "))
address = input("Enter your address: ")

print("User Information")

success = Airtel(name,age,gender,email,contact,address)
success.display()

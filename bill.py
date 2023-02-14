a = (input("enter your here: "))
print("Name: ",a)

b = (input("Enter your gender: "))
print("gender:",b)

Age = int(input("Please Enter Your Age Here: "))
print("Your Age IS: ", Age)

rate = float(input("Enter Rate : "))

amount = rate
print("Amount = ",amount)

if(amount >= 100000):
    discount = 20
elif(amount>=50000 and amount<=99999):
   discount = 10
else:
   discount = 5

discountAmount = (amount*discount)/100
netAmt = amount - discountAmount

print("Discount = %d%% and Discount Amount = %.2f"%(discount,discountAmount))

print("Net Amount = ",netAmt) 

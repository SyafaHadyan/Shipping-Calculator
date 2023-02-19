User_Input = float(input("Product Price:"))

Price = User_Input
Discount = 0
Shipping = 7
Tax = 1

if Price >= 20:
  Shipping = 5
  
elif Price >= 25:
  Shipping = 3

elif Price >= 30:
  Shipping = 1

elif Price >= 35:
  Shipping = 0

elif Price >= 50:
  Shipping = 0
  Discount = 2

elif Price >= 100:
  Shipping = 0
  Discount = 5

else:
  print("Invalid Price value, please insert a number")

Total_Price = Price + Shipping + Tax - Discount

print(f"Price: {Price}")
print(f"Discount: {Discount}")
print(f"Shipping: {Shipping}")
print(f"Tax: {Tax}")
print(f"Total: {Total_Price}")
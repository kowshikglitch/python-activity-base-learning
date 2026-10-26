names = []
amounts = []
n = int(input("How many products? "))
 
for i in range(n):
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    names.append(name)
    amounts.append(price * qty)
 
subtotal = sum(amounts)
 
if subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0
 
tax = (subtotal - discount) * 0.05
total = subtotal - discount + tax
 
print("\\n--- INVOICE ---")
for i in range(n):
    print(names[i], ": ₹", round(amounts[i], 2))
print("Subtotal: ₹", round(subtotal, 2))
print("Discount: ₹", round(discount, 2))
print("Tax: ₹", round(tax, 2))
print("Final amount: ₹", round(total, 2))

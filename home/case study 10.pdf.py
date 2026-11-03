products = []
n = int(input("Number of products: "))
 
for i in range(n):
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    received = int(input("Received quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    actual = int(input("Actual closing stock: "))
 
    expected = opening + received - dispatched
    difference = actual - expected
    products.append((name, expected, actual, difference))
 
print("\\n--- STOCK REPORT ---")
for name, expected, actual, difference in products:
    print(name, "| Expected:", expected, "| Actual:", actual)
    if difference == 0:
        print("Status: Matched")
    elif difference < 0:
        print("Status: Shortage of", abs(difference))
    else:
        print("Status: Surplus of", difference)

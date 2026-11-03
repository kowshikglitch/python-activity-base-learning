balance = float(input("Opening balance: "))
transactions = []
 
while True:
    kind = input("Enter D=deposit, W=withdraw, 0=finish: ").upper()
    if kind == "0":
        break
 
    if kind != "D" and kind != "W":
        print("Invalid transaction type.")
        continue
 
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Amount must be positive.")
    elif kind == "D":
        balance += amount
        transactions.append(("Deposit", amount))
        print("Deposit successful.")
    elif amount <= balance:
        balance -= amount
        transactions.append(("Withdrawal", amount))
        print("Withdrawal successful.")
    else:
        print("Rejected: insufficient balance.")
 
print("\\nTransactions:")
for kind, amount in transactions:
    print(kind, "₹", round(amount, 2))
print("Final balance: ₹", round(balance, 2))

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
overtime = float(input("Enter overtime pay: "))
incentive = float(input("Enter incentive: "))
 
hra = basic * 0.20
allowance = basic * 0.10
gross = basic + hra + allowance + overtime + incentive
 
if gross <= 30000:
    rate = 0.05
else:
    rate = 0.10
 
deduction = gross * rate
net = gross - deduction
 
print("\\n--- SALARY STATEMENT ---")
print("Employee:", name)
print("Gross salary: ₹", round(gross, 2))
print("Deduction: ₹", round(deduction, 2))
print("Net salary: ₹", round(net, 2))

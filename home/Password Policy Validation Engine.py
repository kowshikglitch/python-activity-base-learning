password = input("Enter a sample password: ")
has_upper = False
has_lower = False
has_digit = False
 
for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
 
valid = True
if len(password) < 8:
    print("Failed: must contain at least 8 characters.")
    valid = False
if not has_upper:
    print("Failed: add an uppercase letter.")
    valid = False
if not has_lower:
    print("Failed: add a lowercase letter.")
    valid = False
if not has_digit:
    print("Failed: add a digit.")
    valid = False
 
if valid:
    print("Password meets the classroom rules.")
else:
    print("Password does not meet the rules.")

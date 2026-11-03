attended = int(input("Classes attended: "))
total = int(input("Total classes held: "))
target = 75
 
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details.")
else:
    percentage = attended / total * 100
    extra = 0
 
    while (attended + extra) / (total + extra) * 100 < target:
        extra += 1
 
    print("Current attendance:", round(percentage, 2), "%")
    print("More classes to attend:", extra)
    print("Target attendance:", target, "%")

rows = int(input("Number of rows: "))
cols = int(input("Seats per row: "))
reserved = input("Reserved seats (example 1-2,2-3), or none: ")
reserved_seats = []
 
if reserved.lower() != "none" and reserved.strip() != "":
    for item in reserved.split(","):
        reserved_seats.append(item.strip())
 
print("\\nR = Reserved seat")
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        seat = str(r) + "-" + str(c)
        if seat in reserved_seats:
            print("R", end="\\t")
        else:
            print(seat, end="\\t")
    print()

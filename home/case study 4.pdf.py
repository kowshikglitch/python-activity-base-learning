marks = []
for i in range(5):
    mark = int(input("Enter mark for subject " + str(i + 1) + ": "))
    marks.append(mark)
 
valid = True
for mark in marks:
    if mark < 0 or mark > 100:
        valid = False
 
if not valid:
    print("Invalid marks: each mark must be 0 to 100.")
else:
    grace = 5
    final_marks = marks.copy()
 
    for i in range(5):
        if 30 <= final_marks[i] < 35:
            needed = 35 - final_marks[i]
            if needed <= grace:
                final_marks[i] += needed
                grace -= needed
 
    total = sum(final_marks)
    average = total / 5
    print("Final marks:", final_marks)
    print("Total:", total, "/ 500")
    print("Average:", round(average, 2), "%")
 
    if all(mark >= 35 for mark in final_marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")

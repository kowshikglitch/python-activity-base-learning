names = []
marks = []
n = int(input("Number of students: "))
subjects = ["Python", "Maths", "English"]
 
for i in range(n):
    name = input("Student name: ")
    row = []
    for subject in subjects:
        score = float(input(name + " - " + subject + " marks: "))
        row.append(score)
    names.append(name)
    marks.append(row)
 
totals = []
print("\\n--- STUDENT REPORT ---")
for i in range(n):
    total = sum(marks[i])
    average = total / len(subjects)
    totals.append(total)
    print(names[i], "Marks:", marks[i],
          "Total:", total, "Average:", round(average, 2))
 
if n > 0:
    top = totals.index(max(totals))
    print("Top student:", names[top], "with total", totals[top])
 
for j in range(len(subjects)):
    subject_total = 0
    for i in range(n):
        subject_total += marks[i][j]
    if n > 0:
        print(subjects[j], "average:", round(subject_total / n, 2))

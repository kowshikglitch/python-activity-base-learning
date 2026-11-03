name = input("Student name: ")
scores = []
 
for exam in range(3):
    score = float(input("Enter exam " + str(exam + 1) + " score: "))
    scores.append(score)
 
average = sum(scores) / len(scores)
change = scores[-1] - scores[0]
 
if change > 0:
    trend = "Improved"
elif change < 0:
    trend = "Declined"
else:
    trend = "Unchanged"
 
print("\\nStudent:", name)
print("Scores:", scores)
print("Average score:", round(average, 2))
print("Change from first to last exam:", round(change, 2))
print("Performance trend:", trend)

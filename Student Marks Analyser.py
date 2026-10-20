print("STUDENT MARKS ANALYZER")

name = input("Enter student name: ")
marks = []

for i in range(3):
    mark = int(input(f"Enter subject {i+1} marks: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("\nStudent:", name)
print("Total:", total)
print("Average:", average)

if average >= 85:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")
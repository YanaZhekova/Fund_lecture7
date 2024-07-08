lines = int(input())
students_academy = dict()
for i in range(lines):
    student_name = input()
    grade = float(input())

    if student_name not in students_academy:
        students_academy[student_name] = list()
        students_academy[student_name].append(grade)
    else:
        students_academy[student_name].append(grade)

for s_a in students_academy.keys():
    average_grade = sum(students_academy[s_a]) / len(students_academy[s_a])
    if average_grade >= 4.5:
        print(f"{s_a} -> {average_grade:.2f}")

command = input()
courses = dict()

while ":" in command:

    data = command.split(":")
    name_student = data[0]
    id_student = int(data[1])
    course = data[2]
    if course not in courses:
        courses[course] = dict()
        courses[course][id_student] = name_student
    else:
        courses[course][id_student] = name_student

    command = input()
course = command.replace("_", " ")
for c in courses.keys():
    if c == course:
        info = courses[c]
        for i in courses[c].keys():
            id = i
            name = courses[c][i]
            print(f"{name} - {id}")

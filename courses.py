command = input()
courses = dict()

while command != "end":
    course = command.split(" : ")[0]
    name = command.split(" : ")[1]

    if course not in courses:
        courses[course] = list()
        courses[course].append(name)
    else:
        courses[course].append(name)

    command = input()


for c in courses.keys():
    print(f"{c}: {len(courses[c])}")
    for n in courses[c]:
        print(f"-- {n}")
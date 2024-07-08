command = input()
companies = dict()
while command != "End":
    company_names = command.split(" -> ")[0]
    employees_id = command.split(" -> ")[1]

    if company_names not in companies:
        companies[company_names] = list()
        companies[company_names].append(employees_id)
    else:
        if employees_id not in companies[company_names]:
            companies[company_names].append(employees_id)

    command = input()

for c in companies:
    print(f"{c}")
    for i in companies[c]:
        print(f"-- {i}")
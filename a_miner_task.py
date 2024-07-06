command = input()
resources = dict()

while command != "stop":
    quantity = int(input())
    if command not in resources:
        resources[command] = quantity
    else:
        resources[command] += quantity

    command = input()

for k in resources:
    print(f"{k} -> {resources[k]}")

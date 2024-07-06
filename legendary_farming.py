info = input().split(" ")

items = dict()
is_obtained = False
while not is_obtained:
    for i in range(0, len(info), 2):
        quantity = int(info[i])
        item = info[i + 1].lower()

        if item in items:
            items[item] += quantity
        else:
            items[item] = quantity

    for i in items.keys():
        if items[i] >= 250:
            items[i] -= 250
            if i == "shards":
                print("Shadowmourne obtained!")
            elif i == "motes":
                print("Dragonwrath obtained!")
            elif i == "fragments":
                print("Valanyr obtained!")
            is_obtained = True

    info = input().split(" ")

for i in items.keys():
    if i == "shards":
        print(f"{i}: {items[i]}")
    elif i == "fragments":
        print(f"{i}: {items[i]}")
    elif i == "motes":
        print(f"{i}: {items[i]}")

for i in items.keys():
    if i != "shards" and i != "fragments" and i != "motes":
        print(f"{i}: {items[i]}")


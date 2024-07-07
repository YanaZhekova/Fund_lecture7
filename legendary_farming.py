info = input().split(" ")

items = dict()
is_obtained = False
while True:
    for i in range(0, len(info), 2):
        quantity = int(info[i])
        item = info[i + 1].lower()

        if item in items:
            items[item] += quantity
        else:
            items[item] = quantity

        if item == "shards" and items[item] >= 250:
            print("Shadowmourne obtained!")
            items[item] -= 250
            is_obtained = True
            break
        elif item == "motes" and items[item] >= 250:
            print("Dragonwrath obtained!")
            items[item] -= 250
            is_obtained = True
            break
        elif item == "fragments" and items[item] >= 250:
            print("Valanyr obtained!")
            items[item] -= 250
            is_obtained = True
            break

    if is_obtained:
        break
    info = input().split(" ")

for a in range(3):
    if a == 0:
        item = "shards"
        if item in items.keys():
            print(f"{item}: {items[item]}")
        else:
            print(f"{item}: 0")
    elif a == 1:
        item = "fragments"
        if item in items.keys():
            print(f"{item}: {items[item]}")
        else:
            print(f"{item}: 0")
    elif a == 2:
        item = "motes"
        if item in items.keys():
            print(f"{item}: {items[item]}")
        else:
            print(f"{item}: 0")

for i in items.keys():
    if i != "shards" and i != "fragments" and i != "motes":
        print(f"{i}: {items[i]}")

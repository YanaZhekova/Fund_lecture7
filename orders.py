info = input()
items = dict()
while info != "buy":
    item_data = info.split(" ")
    item = item_data[0]
    price = float(item_data[1])
    quantity = int(item_data[2])

    if item in items:
        items[item][0]=price
        items[item][1] += quantity
    else:
        items[item] = list()
        items[item].append(price)
        items[item].append(quantity)

    info = input()

for item in items.keys():

    price = float(items[item][0])
    quantity = int(items[item][1])
    print(f"{item} -> {(price * quantity):.2f}")

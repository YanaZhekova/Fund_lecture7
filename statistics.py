command = input()

stock = dict()

while ":" in command:
    info = command.split(":")
    product = info[0]
    quantity = int(info[1])
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

    command = input()

print("Products in stock:")
for product in stock.keys():
    print(f"- {product}: {stock[product]}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")

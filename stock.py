text = input().split(" ")
stock = dict()

for i in range(0, len(text), 2):
    product = text[i]
    quantity = int(text[i + 1])
    stock[product] = quantity

searched_products = input().split(" ")
for product in searched_products:
    if product not in stock:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {stock[product]} of {product} left")


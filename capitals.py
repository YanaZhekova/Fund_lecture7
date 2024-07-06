countries = input().split(", ")
capitals = input().split(", ")

for cou, cap in zip(countries, capitals):
    print(f"{cou} -> {cap}")


info = input()
phonebook = dict()

while "-" in info:
    name = info.split("-")[0]
    phone_number = info.split("-")[1]
    phonebook[name] = phone_number

    info = input()

number = int(info)

for i in range(number):
    find_name = input()
    if find_name in phonebook.keys():
        print(f"{find_name} -> {phonebook[find_name]}")
    else:
        print(f"Contact {find_name} does not exist.")

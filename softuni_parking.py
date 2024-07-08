number = int(input())
parking_book = dict()

for i in range(number):
    command_info = input().split(" ")
    command = command_info[0]
    name = command_info[1]

    if command == "register":
        license_plate_number = command_info[2]
        if name not in parking_book:
            parking_book[name] = list()
            parking_book[name].append(license_plate_number)
            print(f"{name} registered {license_plate_number} successfully")
        else:
            if license_plate_number in parking_book[name]:
                print(f"ERROR: already registered with plate number {license_plate_number}")
            else:
                parking_book[name].append(license_plate_number)
    elif command == "unregister":
        if name not in parking_book:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking_book.pop(name)

for i in parking_book.keys():
    plate_numbers = " ".join(parking_book[i])
    print(f"{i} => {plate_numbers}")

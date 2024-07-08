command = input()
force_book = dict()

while command != "Lumpawaroo":
    exist_user = False
    if "|" in command:
        command_info = command.split(" | ")
        force_side = command_info[0]
        force_user = command_info[1]
        if force_side not in force_book:
            force_book[force_side] = list()
            force_book[force_side].append(force_user)
        else:
            for f in force_book.keys():
                for n in force_book[f]:
                    if force_user == n:
                        exist_user = True
            if not exist_user:
                force_book[force_side].append(force_user)
    elif "->" in command:
        command_info = command.split(" -> ")
        force_side = command_info[1]
        force_user = command_info[0]
        if force_side not in force_book:
            force_book[force_side] = list()
            force_book[force_side].append(force_user)
        else:
            for f in force_book.keys():
                for n in force_book[f]:
                    if force_user == n:
                        exist_user = True
                        force_book[force_side].append(force_user)
                        index = force_book[f].index(force_user)
                        force_book[f].pop(index)

            if not exist_user:
                force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")
    command = input()

for f in force_book.keys():
    if len(force_book[f]) != 0:
        print(f"Side: {f}, Members: {len(force_book[f])}")
        for n in force_book[f]:
            print(f"! {n}")

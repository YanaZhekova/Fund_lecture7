text = input()
chars = dict()

for c in text:
    if c != " ":
        count_char = text.count(c)
        chars[c] = count_char

for k in chars:
    print(f"{k} -> {chars[k]}")
characters = input().split(", ")
ascii_values = dict()

for char in characters:
    ascii_values[char] = ord(char)

print(ascii_values)
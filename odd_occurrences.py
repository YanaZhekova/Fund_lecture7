words = input().split(" ")
count_words = dict()
words = list(w.lower() for w in words)

for word in words:
    count = words.count(word)
    if count % 2 == 1:
        count_words[word] = count

print(" ".join(count_words.keys()))

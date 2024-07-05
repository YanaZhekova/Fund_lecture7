number = int(input())
words_synonyms = dict()

for i in range(number):
    word = input()
    synonym = input()
    if word not in words_synonyms:
        words_synonyms[word]=list()
        words_synonyms[word].append(synonym)
    else:
        words_synonyms[word].append(synonym)

for k in words_synonyms.keys():
    list_of_synonyms = ", ".join(words_synonyms[k])
    print(f"{k} - {list_of_synonyms}")

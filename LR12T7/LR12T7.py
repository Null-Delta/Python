file = open("LR12T7/file.txt", "r")

text = file.read().lower()

text = text.replace("/n", " ")
text = text.replace(",", " ")
text = text.replace(".", " ")
textWords = text.split()

words = {}

for word in textWords:
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

print(sorted(words.items(), key = lambda item: item[1], reverse=True)[0][0])
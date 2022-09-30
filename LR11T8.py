# variant 8
n = int(input())

engToLat = {}
LatToEng = {}

for index in range(n):
    inp = input().replace(" ", "").split("-")
    latWords = inp[1].split(",")
    engToLat[inp[0]] = latWords
    for word in latWords:
        if word in LatToEng.keys():
            LatToEng[word].append(inp[0])
        else:
            LatToEng[word] = [inp[0]]

print()

for item in sorted(LatToEng.items(),key=lambda item: item):
    print(item[0] + " - " + ", ".join(item[1]))
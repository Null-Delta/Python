# variant 1

print(len(set(input().split())))

# variant 6
n = int(input())
words = set()

for i in range(n):
    newWords = input().split()
    for word in newWords:
        words.add(word)

print(len(words))

# variant 10
n, k = input().split()
days = set()

for i in range(int(k)):
    a, b = input().split()
    day = int(a);
    while day < int(n):
        days.add(day)
        day += int(b)

print(len(days))
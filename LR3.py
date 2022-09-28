# variant 5

start = 9 * 60
lesson = int(input())
start += lesson * 45
for i in range(1,lesson):
    start += 5 if i % 2 == 1 else 15
print(start // 60, start % 60, sep=":")

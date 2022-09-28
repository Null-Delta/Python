# variant 2
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

can = abs(x1 - x2) + abs(y1 - y2) == 1
print("Yes" if can else "No")
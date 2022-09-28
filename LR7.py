# variant 16

positions = [];
for i in range(0,8):
    inputPosition = input().split()
    positions.append((int(inputPosition[0]), int(inputPosition[1])))

isHit = False
for i in range(0,8):
    for j in range(i + 1,8):
        if (positions[i][0] == positions[j][0] or positions[i][1] == positions[j][1]):
            isHit = True

print("YES" if isHit else "NO")

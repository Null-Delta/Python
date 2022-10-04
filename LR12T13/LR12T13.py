lines = open("LR12T13/file.txt", "r").read().split("\n")

elements = list(map(lambda line: (line.split()[1], line.split()[2]), lines))

print(elements)

inp = input()

while(len(inp) != 0):
    print(elements[int(inp)])
    inp = input()
    
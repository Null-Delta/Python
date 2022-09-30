# variant 11

n = int(input())

tree = {}
cheliki = []

for index in range(n - 1):
    inp = input().split()
    if inp[1] in tree.keys():
        tree[inp[1]].append(inp[0])
    else:
        tree[inp[1]] = [inp[0]]

def isParent(key):
    for item in tree.items():
        if key in item[1]:
            return False
    return True

def findChels(chel, lvl):
    cheliki.append((chel, lvl))
        
    if chel in tree.keys():
        for chelik in tree[chel]:
            findChels(chelik, lvl + 1)
    
root = list(filter(isParent, tree.keys()))[0]

findChels(root, 0)
print()

for chel in sorted(cheliki):
    print(chel[0] + " " + str(chel[1]))
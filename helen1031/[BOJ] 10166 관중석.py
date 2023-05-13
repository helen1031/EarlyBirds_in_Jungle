import sys
input = sys.stdin.readline

d1, d2 = map(int, input().split())

angles = set()

for r in range(d1, d2+1):
    interval = 360 / r
    for i in range(r):
        pos = i * interval
        if pos in angles:
            continue
        else:
            angles.add(pos)

print(len(angles))
import sys
input = sys.stdin.readline

mdict = {"D": [(2, 0), (3, 1), (0, 2), (1, 3)],
         "U": [(0, 2), (1, 3), (2, 0), (3, 1)],
         "R": [(1, 0), (0, 1), (3, 2), (2, 3)],
         "L": [(0, 1), (1, 0), (2, 3), (3, 2)]}

k = int(input())
methods = list(map(str, input().rstrip().split()))
hole_pos = int(input())

answer = [[0] * (2 ** k) for _ in range(2 ** k)]

y, x = 1, 1
for method in methods:
    if method == "D":
        y =
    elif method == "U":
    elif method == "R":
    else:
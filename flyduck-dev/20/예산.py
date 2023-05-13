import sys
input = sys.stdin.readline
N = int(input()) #3 이상 10,000 이하 : 4
arr = list(map(int,input().split())) #: 120 110 140 150
M = int(input())
start = 0
end = max(arr)
mid = 0
tot = 0
res = 0
while(start <= end):
    tot = 0
    mid = (start + end) // 2
    for i in range(len(arr)):
        if arr[i] < mid:
            tot += arr[i]
        else:
            tot += mid
    if tot < M:
        res = mid
        start = mid+1
    elif tot > M:
        end = mid -1
    else:
        res = mid
        break
print(res)
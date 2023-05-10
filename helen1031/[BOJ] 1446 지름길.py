import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, d = map(int, input().split())
distance = [INF] * (d+1)

graph = [[] for i in range(d+1)]
for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= d:
        graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0))
    distance[0] = 0

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for i in graph[cur]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])
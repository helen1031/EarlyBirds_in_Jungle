import sys
input = sys.stdin.readline
# k가 2일 때만 통과되어서 부분점수 9점
K = int(input())
C = int(input()) 
for _ in range(C):
    answer = 0
    M,N = map(int,input().split()) 
    if M == N:
        print(1)
    elif M>N:
        rest_chance = K-N
        if M > rest_chance + N:
            print(0)
        else:
            print(1)
    elif M<N:
        rest_chance = K-N
        if N-M == 1:
            print(1)
        elif M+rest_chance < N:
            print(0)
        else:
            print(1)
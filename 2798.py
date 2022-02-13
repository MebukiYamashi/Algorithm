import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Deck = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if Deck[i] + Deck[j] + Deck[k] > M:
                continue
            else:
                result = max(result, Deck[i] + Deck[j] + Deck[k])
print(result)

"""
3중 for문을 돌려서 M에 가장 가까운 수 또는 M을 찾으면 되므로
i, j, k에 대한 모든 탐색을 수행

"""
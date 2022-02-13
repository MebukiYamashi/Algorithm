import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(0, N + 1):
    arr = list(map(int, str(i)))
    result = i + sum(arr)
    if result == N:
        print(i)
        break
    if i == N:
        print(0)
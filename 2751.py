import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr = sorted(arr)

for i in arr:
    print(i)
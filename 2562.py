import sys
input = sys.stdin.readline
arr = []
for _ in range(9):
    N = int(input())
    arr.append(N)
print(max(arr))
print(arr.index(max(arr))+1) #Index Number니까 +!

import sys
input = sys.stdin.readline

temp = N = int(input())
cnt = 0

while True:
    a = temp // 10
    b = temp % 10
    summy = (a + b) % 10
    temp = (b * 10) + summy
    cnt += 1
    if N == temp:
        break
print(cnt)
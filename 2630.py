import sys
input = sys.stdin.readline

n = int(input())
paper = []

for _ in range(n):
    row = list(map(int, input().rsplit()))
    paper.append(row)

white, blue = 0, 0

def check(row, col, n):
    global white, blue
    color = paper[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if color != paper[i][j]:
                next = n // 2
                check(row, col, next)
                check(row, col + next, next)
                check(row + next, col, next)
                check(row + next, col + next, next)
                return

    if color == 0:
        white += 1
    else:
        blue += 1
    return

check(0, 0, n)
print(white)
print(blue)

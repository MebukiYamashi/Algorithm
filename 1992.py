import sys
input = sys.stdin.readline

N = int(input())
image = [list(map(int, input().rstrip())) for _ in range(N)]

def pixelcomp(x, y, n):

    check = image[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != image[i][j]:
                print('(', end = '')
                pixelcomp(x, y, n // 2) # 우상단
                pixelcomp(x, y + n // 2, n // 2) #좌상단
                pixelcomp(x + n // 2, y, n // 2) #우하단
                pixelcomp(x + n // 2, y + n // 2, n // 2) #좌하단
                print(')', end = '')
                return

    if check == 0:
        print('0', end = '')
        return
    else:
        print('1', end = '')
        return

pixelcomp(0, 0, N)

"""
sys.stdin.readline 함수는 input을 받을 때 각각 지정해줘야하는 부분이 다르다
문자열의 경우 sys.stdin.readline()
정수형은 int(sys.stdin.readline()
여러개를 받을 때는 map(_type, sys.stdin.readline().split()

이 문제에서는 list에 문자열(정수형)을 n줄 받아야했는데 
여기서 sys.stdin.readline함수가 개행문자를 포함하게 되므로
sys.stdin.readline().strip() <- strip을 사용해 개행문자를 제거해줘야한다.

이외 부분은 2630번의 분할정복 기법과 동일
각 사분면에서 모두 0이거나 1일때 제외하면 4분할 트리 돌면서 정렬한다
"""
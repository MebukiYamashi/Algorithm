import sys
input = sys.stdin.readline

a = int(input()) * int(input()) * int(input())
for i in range(10):
    print(str(a).count(str(i)))


"""
이쁜 코딩을 위해 변수 3개를 안 받고 그ㅡ냥 input 3개를 곱해서 list를 만듦
int형이니 count를 쓰기위해 str으로 바꿔줘야함
"""
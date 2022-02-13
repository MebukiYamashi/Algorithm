from collections import deque
N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  graph[m1][m2] = graph[m2][m1] = 1

def bfs(start_from_v):
   arrive = [start_from_v]
   queue = deque()
   queue.append(start_from_v)

   while queue:
        v = queue.popleft()
        print(v, end = '')

        for w in range(len(graph[start_from_v])):
            if graph[v][w] == 1 and (w not in arrive):
                arrive.append(w)
                queue.append(w)


def dfs(start_from_v, arrive=[]):
    arrive.append(start_from_v)
    print(start_from_v, end = '')

    for w in range(len(graph[start_from_v])):
        if graph[start_from_v][w] == 1 and (w not in arrive):
            dfs(w, arrive)
dfs(V)
print()
bfs(V)
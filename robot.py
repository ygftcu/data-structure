import sys
from collections import deque

def input():
    return sys.stdin.readline()

n,m = map(int,input().split())
r,c,d = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 0 , 1 , 0]
dy = [0, 1,0,-1]

count = 0

def bfs(x,y,d) :
    global count
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    count += 1

    while q:
        x, y = q.popleft()
        turn = 0
        #이거 몰라서 오지게 찾아봄 로봇 방향 돌리기
        for i in range(4):
            d = (d + 3) % 4
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not room[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    turn = 1
                    count += 1
                    break
        if turn == 0:
            bx, by = x - dx[d], y - dy[d]
            if room[bx][by] == 1:
                print(count)
                break
            else:
                q.append((bx, by))

bfs(r, c, d)
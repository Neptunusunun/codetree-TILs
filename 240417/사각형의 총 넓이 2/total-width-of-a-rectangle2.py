n = int(input())

graph = [ [0 for _ in range(200)] for _ in range(200)]

for _ in range(n):

    x1,y1,x2,y2 = list(map(int,input().split()))
    x1,y1,x2,y2 = x1+100,y1+100,x2+100,y2+100

    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j] = 1


ans = 0
for i in range(200):
    for j in range(200):
        ans += graph[i][j]

print(ans)
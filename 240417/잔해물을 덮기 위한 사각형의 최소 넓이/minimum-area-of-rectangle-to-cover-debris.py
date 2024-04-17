x1,y1,x2,y2 = list(map(int,input().split()))
a1,b1,a2,b2 = list(map(int,input().split()))

x1,y1,x2,y2 = x1+1000,y1+1000,x2+1000,y2+1000
a1,b1,a2,b2 = a1+1000,b1+1000,a2+1000,b2+1000

graph = [ [ 0 for _ in range(2000)] for _ in range(2000)]
check= False
#첫번째 사각형 넓이 표시
for i in range(x1,x2):
    for j in range(y1,y2):
        graph[i][j] = 1

#두번째 사각형 겹치는 부분 0으로 빼기
for i in range(a1,a2):
    for j in range(b1,b2):
        graph[i][j] = 0
        check = True

#최소 최대 x1y1 x2y2로 최소 직사각형 넓이 구하기

m1,m2,n1,n2 = 2001,-1,-1,2001
for i in range(x1,x2):
    for j in range(y1,y2):
        if graph[i][j] == 1:
            m1 = min(m1,i)
            n1 = max(n1,j)
            m2 = max(m2,i)
            n2 = min(n2,j)

size = (m2-m1+1)*(n1-n2+1)

if check:
    print(size)
else:
    print(0)
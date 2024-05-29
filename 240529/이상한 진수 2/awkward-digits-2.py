a = list(map(int,list(input())))

i = 0
if 0 in a:
    while a[i] == 1:
        i += 1
    a[i] = 1

else:
    a[-1] = 0

#이진수 변환하기
answer = 0
for j in range(len(a)-1,0,-1):
    answer += (2**j) * a[len(a)-1-j]

print(answer)
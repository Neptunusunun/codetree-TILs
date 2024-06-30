a,b,c,d = map(int,input().split())




if (b >= c and a < d)or (d >= a and c < b) :
    print("intersecting")
else: 
    print("nonintersecting")
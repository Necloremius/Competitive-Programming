count = int(input())
for x in range(count):
    x,y,n = map(int,input().split())
    for k in range(n+1,0,-1):
        if k%x==y:
            print(k)
            break

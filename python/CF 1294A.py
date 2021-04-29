d = int(input())
for x in range(d):
    a,b,c,n = map(int,input().split())
    average = (a+b+c+n)//3
    if (a+b+c+n)%3==0 and average >= max(a,b,c):
        print("YES")
    else:
        print("NO")

n = int(input())
for x in range(n):
    sum=0
    a = int(input())
    if a%2050==0:
        a //= 2050
        for i in str(a):
            sum+=int(i)
        print(sum)
    else:
        print(-1)

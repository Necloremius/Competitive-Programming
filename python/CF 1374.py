count = int(input())
for _ in range(count):
    x,y,n = map(int,input().split())
    if n % x == y:
        print(n)
    elif n % x > y:
        print(n - (n % x) + y)
    else:
        print((n - (n % x))-x+y)

n = int(input())
for x in range(n):
    a = int(input())
    if a < 3:
        print(0)
    else:
        print(a//2+a%2-1)

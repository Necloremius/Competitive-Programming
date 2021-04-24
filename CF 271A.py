x = int(input())
for y in range(2000000):
    if y>x:
        if len(set(str(y)))==4:
            print(y)
            break

a = int(input())
for i in range(a):
    x = list(input())
    if len(x)>10:
        print(f"{x[0]}{len(x)-2}{x[-1]}")
    else:
        print(''.join(x))

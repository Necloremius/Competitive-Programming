x = int(input())
a = str(x)
if a[-1] == '0' or a[-1] == '5':
    print(int(x/5))
elif a[-1] == '1' or a[-1] == '2' or a[-1] == '3' or a[-1] == '4':
    print(int((x-int(a[-1]))/5 + 1))
elif a[-1] == '6' or a[-1] == '7' or a[-1] == '8' or a[-1] == '9':
    print(int((x-int(a[-1]))/5 + 2))

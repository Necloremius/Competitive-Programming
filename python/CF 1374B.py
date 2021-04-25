n = int(input())
for x in range(n):
    a = int(input())
    counter=0
    while a%6==0:
        a = a//6
        counter+=1
    while a%3==0:
        a = a//3
        counter+=2

    if a==1:
        print(counter)
    else:
        print(-1)
